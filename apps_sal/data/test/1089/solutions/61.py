N, M, K = map(int, input().split())
mod = int(1e9) + 7
fact = [1 for _ in range(N*M+1)]
invf = [1 for _ in range(N*M+1)]
def inved(a):
  x, y, u, v, k, l = 1, 0, 0, 1, a, mod
  while l != 0:
    x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
    k, l = l, k % l
  return x % mod
for i in range(N*M):
  fact[i+1] = (fact[i] * (i + 1)) % mod
invf[-1] = inved(fact[-1])
for i in range(N*M, 0, -1):
  invf[i-1] = (invf[i] * i) % mod
Z = (fact[M*N-2] * invf[K-2] * invf[M*N-K]) % mod
X = M * (N + 1) * (N - 1)
X %= mod
Y = N * (M + 1) * (M - 1)
Y %= mod
XY = (inved(6) * M * N * (X + Y)) % mod
print((XY * Z) % mod)
