import math
n, a, b = map(int, input().split())
h = [int(input()) for i in range(n)]


def explode(x):
    nonlocal n
    c = 0
    for i in range(n):
        if h[i] - x * b > 0:
            c += math.ceil((h[i] - x * b) / (a - b))
    return c <= x

# 二分探索用のコード


# (1)l,rは両端点でl<=r
l, r = 0, 10**9
# (2)l=rもしくはl=r-1のときにbreak
while l + 1 < r:
    # (3)その閉区間の中点(の小数部分を切り捨てたもの)
    # オーバーフローを考慮すると以下の書き方になる
    k = l + (r - l) // 2
    # ここでは境目以上のxで真になるので、
    # x=kで真の場合は大きい方の端点をkにし、x=kで偽の場合は小さい方の端点をkにする
    if explode(k):
        r = k
    else:
        l = k

print(r)
