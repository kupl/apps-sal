def i_input(): return int(input())


def i_map(): return list(map(int, input().split()))


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


def bit_search(n, list_n):

    bit_ans = []
    for _ in range(2**n):
        t = [0] * n
        bit_ans.append(t)
    for i in range(2 ** n):
        for j in range(n):
            if ((i >> j) & 1):
                bit_ans[i][j] = list_n[j]

    return bit_ans


cost = 10**18
n, m, x = i_map()
caa = i_row_list(n)
ls = list(range(1, n + 1))
bls = bit_search(n, ls)
for bb in bls:
    ch = [0] * (m + 1)
    for i in range(n):
        if bb[i] != 0:
            ch = [c + b for (c, b) in zip(ch, caa[bb[i] - 1])]
    for i in range(m + 1):
        if i == 0:
            flg = 1
            tmp = ch[i]
        else:
            if ch[i] < x:
                flg = 0
    if flg == 1:
        cost = min(cost, tmp)
if cost == 10**18:
    cost = -1
print(cost)
