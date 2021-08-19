def pow3(a):
    return 0 if a == -1 else p[a]


afdsfasdf = int(input())
s = list(input())
n = len(s)
mod = pow(10, 9) + 7
x = [[0] * 2 for _ in range(n - 1)]
y = [[0] * 2 for _ in range(n - 1)]
p = [1] * n
ans = 0
for i in range(1, n):
    p[i] = 3 * p[i - 1] % mod
for i in range(n - 2):
    if s[i] == 'a':
        x[i + 1][0] = 1
    elif s[i] == '?':
        x[i + 1][1] = 1
    for j in range(2):
        x[i + 1][j] += x[i][j]
    k = n - i - 1
    if s[k] == 'c':
        y[i + 1][0] = 1
    elif s[k] == '?':
        y[i + 1][1] = 1
    for j in range(2):
        y[i + 1][j] += y[i][j]
for i in range(n - 2):
    (j, k) = (i + 1, n - i - 2)
    if s[j] == 'b' or s[j] == '?':
        c1 = (x[j][0] * pow3(x[j][1]) + x[j][1] * pow3(x[j][1] - 1)) % mod
        c2 = (y[k][0] * pow3(y[k][1]) + y[k][1] * pow3(y[k][1] - 1)) % mod
        ans += c1 * c2
        ans %= mod
print(ans)
