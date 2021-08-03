n, m = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
MOD = 10**9 + 7
sx, sy = 0, 0
for i in range(n):
    t = 2 * i + 1 - n
    t *= X[i]
    t %= MOD
    sx += t
    sx %= MOD
for j in range(m):
    t = 2 * j + 1 - m
    t *= Y[j]
    t %= MOD
    sy += t
    sy %= MOD
print(sx * sy % MOD)
