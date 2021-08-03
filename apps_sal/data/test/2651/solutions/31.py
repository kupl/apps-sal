n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = int(1e9) + 7
S = 0
for i in range(n):
    S += (2 * i + 1 - n) * x[i]
    S %= mod
T = 0
for j in range(m):
    T += (2 * j + 1 - m) * y[j]
    T %= mod
print(S * T % mod)
