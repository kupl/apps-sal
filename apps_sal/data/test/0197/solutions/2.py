import sys
from itertools import chain
readline = sys.stdin.readline

MOD = 998244353


def compress(L):
    L2 = list(set(L))
    L2.sort()
    C = {v: k for k, v in enumerate(L2)}
    return L2, C


N = int(readline())
LR = [tuple(map(int, readline().split())) for _ in range(N)]
LR = [(a - 1, b) for a, b in LR]
LR2 = LR[:]
ml = LR[-1][0]
res = 0
for i in range(N - 2, -1, -1):
    l, r = LR[i]
    if r <= ml:
        break
    l = max(ml, l)
    ml = l
    LR[i] = (l, r)
else:
    Z = list(chain(*LR))
    Z2, Dc = compress(Z)

    NN = len(Z2)
    seglen = [0] + [n - p for p, n in zip(Z2, Z2[1:])]

    hc = [[0] * (N + 3) for _ in range(NN)]
    for j in range(NN):
        hc[j][0] = 1
        for k in range(1, N + 3):
            hc[j][k] = hc[j][k - 1] * pow(k, MOD - 2, MOD) * (seglen[j] - 1 + k) % MOD

    mask = [[[True] * NN]]

    dp = [[[0] * (N + 1) for _ in range(NN + 1)] for _ in range(N + 1)]
    Dp = [[1] * (NN + 1)] + [[0] * (NN + 1) for _ in range(N)]
    for i in range(1, N + 1):
        mask2 = [False] * NN
        l, r = LR[i - 1]
        dl, dr = Dc[l], Dc[r]
        for j in range(dr, dl, -1):
            mask2[j] = True
        mm = [[m1 & m2 for m1, m2 in zip(mask[-1][idx], mask2)] for idx in range(i)] + [mask2]
        mask.append(mm)
        for j in range(NN):
            for k in range(1, i + 1):
                if mask[i][i - k + 1][j]:
                    dp[i][j][k] = Dp[i - k][j + 1] * hc[j][k] % MOD

        for j in range(NN - 1, -1, -1):
            res = Dp[i][j + 1]
            if dl < j <= dr:
                for k in range(1, i + 1):
                    res = (res + dp[i][j][k]) % MOD
            Dp[i][j] = res

    res = Dp[N][0]
    for l, r in LR2:
        res = res * (pow(r - l, MOD - 2, MOD)) % MOD
print(res)
