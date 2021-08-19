import sys
input = sys.stdin.readline
(n, k) = map(int, input().split())
mod = 10 ** 9 + 7
FACT = [1]
for i in range(1, 250 + 1):
    FACT.append(FACT[-1] * i % mod)
FACT_INV = [pow(FACT[-1], mod - 2, mod)]
for i in range(250, 0, -1):
    FACT_INV.append(FACT_INV[-1] * i % mod)
FACT_INV.reverse()


def Combi(a, b):
    if 0 <= b <= a:
        return FACT[a] * FACT_INV[b] % mod * FACT_INV[a - b] % mod
    else:
        return 0


COMBI = [[0] * 251 for i in range(251)]
for a in range(251):
    for b in range(a + 1):
        COMBI[a][b] = Combi(a, b)
POW_K = [1]
POW_K1 = [1]
for i in range(n + 1):
    POW_K.append(POW_K[-1] * k % mod)
    POW_K1.append(POW_K1[-1] * (k - 1) % mod)
DP = [0] * (n + 1)
DP[0] = 1
PLUS = [[0] * (n + 1) for i in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            PLUS[i][j] = (POW_K[i] * COMBI[n - i][j - i] * POW_K1[n - j] - POW_K1[n]) % mod
        else:
            PLUS[i][j] = POW_K[i] * COMBI[n - i][j - i] * POW_K1[n - j] % mod
for yoko in range(n):
    NDP = [0] * (n + 1)
    for i in range(n + 1):
        if DP[i] == 0:
            continue
        for j in range(max(1, i), n + 1):
            NDP[j] = (NDP[j] + PLUS[i][j] * DP[i]) % mod
    DP = NDP
print(DP[-1])
