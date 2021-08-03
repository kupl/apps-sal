N, M = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

MOD = 10 ** 9 + 7

cnt = 0
for i in range(M - 1):
    l = Y[i + 1] - Y[i]
    var = (i + 1) * (M - (i + 1))
    cnt += l * var
    cnt %= MOD

ans = 0
for i in range(N - 1):
    l = X[i + 1] - X[i]
    var = (i + 1) * (N - (i + 1))
    ans += l * var * cnt
    ans %= MOD

print(ans)
