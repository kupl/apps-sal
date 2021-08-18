mod = 10**9 + 7

N = int(input())

X = [1, 1, 1]
Y = [1, 2, 3]
for i in range(3, N + 2):
    x = (X[-1] + Y[i - 3]) % mod
    X.append(x)
    Y.append((Y[-1] + x) % mod)

ans = ((Y[N - 2] * (N - 2) + (Y[N - 1])) * (N - 1) + (N - 1) * Y[N - 2] + 1) % mod
print(ans)
