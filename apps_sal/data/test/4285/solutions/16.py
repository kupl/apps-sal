n = int(input())
s = str(input())

mod = 10**9 + 7

X = [[0] * 4 for _ in range(n + 1)]
for i in range(n):
    for j in range(4):
        X[i + 1][j] = X[i][j]
    if s[i] == 'a':
        X[i + 1][0] += 1
    elif s[i] == 'b':
        X[i + 1][1] += 1
    elif s[i] == 'c':
        X[i + 1][2] += 1
    else:
        X[i + 1][3] += 1

Y = [[0] * 4 for _ in range(n + 1)]
for i in reversed(list(range(n))):
    for j in range(4):
        Y[i][j] = Y[i + 1][j]
    if s[i] == 'a':
        Y[i][0] += 1
    elif s[i] == 'b':
        Y[i][1] += 1
    elif s[i] == 'c':
        Y[i][2] += 1
    else:
        Y[i][3] += 1
c = X[n][3]
ans = 0
for i in range(n):
    if s[i] == 'b':
        ans += X[i + 1][3] * Y[i][3] * pow(3, max(0, c - 2), mod)
        ans += X[i + 1][0] * Y[i][2] * pow(3, c, mod)
        ans += X[i + 1][3] * Y[i][2] * pow(3, max(0, X[i + 1][3] - 1 + Y[i][3]), mod)
        ans += X[i + 1][0] * Y[i][3] * pow(3, max(0, X[i + 1][3] + Y[i][3] - 1), mod)
        ans %= mod
    if s[i] == '?':
        ans += X[i][3] * Y[i + 1][3] * pow(3, max(0, c - 3), mod)
        ans += X[i + 1][0] * Y[i][2] * pow(3, max(0, c - 1), mod)
        ans += X[i][3] * Y[i][2] * pow(3, max(0, X[i][3] - 1 + Y[i + 1][3]), mod)
        ans += X[i + 1][0] * Y[i + 1][3] * pow(3, max(0, X[i][3] + Y[i + 1][3] - 1), mod)
        ans %= mod
        ans %= mod
print(ans)
