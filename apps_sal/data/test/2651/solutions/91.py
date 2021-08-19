(N, M) = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = int(1000000000.0 + 7)
X.sort(reverse=True)
Y.sort(reverse=True)
(XP, YP) = (0, 0)
for i in range(N):
    XP += (N - 1 - i * 2) * X[i]
    XP %= mod
for i in range(M):
    YP += (M - 1 - i * 2) * Y[i]
    YP %= mod
print(XP * YP % mod)
