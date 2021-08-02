import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, M = list(map(int, input().split()))
    bomb = [list([int(x) - 1 for x in input().split()]) for _ in range(M)]
    R = [0] * H
    C = [0] * W

    for h, w in bomb:
        R[h] += 1
        C[w] += 1

    cnt_r = 0
    ma_r = max(R)
    for r in R:
        if r == ma_r:
            cnt_r += 1

    cnt_c = 0
    ma_c = max(C)
    for c in C:
        if c == ma_c:
            cnt_c += 1

    ma = ma_r + ma_c
    cnt_rc = cnt_r * cnt_c
    for h, w in bomb:
        score = R[h] + C[w]
        if score == ma:
            cnt_rc -= 1

    res = ma if cnt_rc else ma - 1
    print(res)


def __starting_point():
    resolve()


__starting_point()
