import sys
input = sys.stdin.readline
mod = 998244353

n, m, k = list(map(int, input().split()))

N = n - 1
INV = [None] * (n + 1)  # 1/aのリストを予め作っておく.
for i in range(1, n + 1):
    INV[i] = pow(i, mod - 2, mod)

# nCkは、nもしくはkが固定の場合はリストで作る

Combi = [None] * (N + 1)  # Combi[i]=nCi を表す
Combi[0] = 1
for i in range(1, N + 1):
    Combi[i] = Combi[i - 1] * (N - i + 1) * INV[i] % mod


ANS = Combi[k] % mod * m % mod * pow(m - 1, k, mod) % mod
print(ANS)
