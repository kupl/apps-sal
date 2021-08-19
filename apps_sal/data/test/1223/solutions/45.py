import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
P = [None] + [int(x) for x in input().split()]
p_to_i = [None] * (N + 1)
for i, x in enumerate(P[1:], 1):
    p_to_i[x] = i

# 大きい数から挿入していく
# 左隣にあるインデックスを取得できるようにしておく
# そのために、[1,i]内で書き込んだ数の個数を獲得できるBITを持つ

# BITは一番最後の1ビットの位置が重要なので0ではなく1始まり。そのためNまでループする


def BIT_add(i):
    while i <= N:
        tree[i] += 1
        i += i & (-i)


def BIT_sum(i):
    s = 0
    while i:
        s += tree[i]
        i -= i & (-i)
    return s


def BIT_search(x):
    # 二分探索。和がx以上となる最小のインデックス(>= 1)を返す
    i = 0
    s = 0
    step = 1 << (N.bit_length() - 1)
    while step:
        if i + step <= N and s + tree[i + step] < x:
            i += step
            s += tree[i]
        step >>= 1
    return i + 1
    left = 0
    right = N
    while right - left > 1:
        mid = (left + right) // 2
        if BIT_sum(mid) >= x:
            right = mid
        else:
            left = mid
    return right


tree = [0] * (N + 1)
answer = 0
for x in range(N, 0, -1):
    c = p_to_i[x]
    L = BIT_sum(c)  # 左にある既に書き込んだ数の個数
    BIT_add(c)
    R = N - x - L  # 右にある既に書き込んだ数の個数
    a = BIT_search(L - 1) if L >= 2 else 0
    b = BIT_search(L) if L >= 1 else 0
    d = BIT_search(L + 2) if R >= 1 else N + 1
    e = BIT_search(L + 3) if R >= 2 else N + 1
    coef = 0
    if b != 0:
        # [b,c]を含むようにする。(a,b) と(c,d)が自由
        coef += (b - a) * (d - c)
    if d != 0:
        # [c,d]を含むようにする。
        coef += (e - d) * (c - b)
    answer += x * coef
print(answer)
