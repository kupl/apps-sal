n, c = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
a, b = [0] * n, [0] * n
a[0] = s[0][1] - s[0][0]
b[0] = s[n - 1][1] - (c - s[n - 1][0])
for i in range(1, n):
    a[i] = a[i - 1] + s[i][1] - (s[i][0] - s[i - 1][0])
    b[i] = b[i - 1] + s[n - 1 - i][1] - (s[n - i][0] - s[n - 1 - i][0])
maxa, maxb = [0] * n, [0] * n
maxa[0], maxb[0] = a[0], b[0]
for i in range(1, n):
    maxa[i] = max(maxa[i - 1], a[i])
    maxb[i] = max(maxb[i - 1], b[i])
ans = max(maxa[n - 1], maxb[n - 1], 0)
for i in range(n - 1):
    ans = max(ans, a[i] + maxb[n - 2 - i] - s[i][0])
    ans = max(ans, b[i] + maxa[n - 2 - i] - (c - s[n - 1 - i][0]))
print(ans)
