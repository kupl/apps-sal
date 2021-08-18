import sys
input = sys.stdin.readline
mod = 998244353

n, m, k = list(map(int, input().split()))

N = n - 1
INV = [None] * (n + 1)
for i in range(1, n + 1):
    INV[i] = pow(i, mod - 2, mod)


Combi = [None] * (N + 1)
Combi[0] = 1
for i in range(1, N + 1):
    Combi[i] = Combi[i - 1] * (N - i + 1) * INV[i] % mod


ANS = Combi[k] % mod * m % mod * pow(m - 1, k, mod) % mod
print(ANS)
