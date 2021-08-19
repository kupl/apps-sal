(n, c) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
now = 0
s = []
t = []
for i in range(n):
    now += a[i][1]
    s.append(now)
now = 0
for i in range(n):
    now += a[n - 1 - i][1]
    t.append(now)
back = 0
ans = max(ans, s[-1] - a[-1][0])
for i in range(n - 2, -1, -1):
    back = max(back, t[n - 2 - i] - 2 * (c - a[i + 1][0]))
    ans = max(ans, s[i] - a[i][0] + back)
back = 0
ans = max(ans, t[-1] - (c - a[0][0]))
for i in range(n - 2, -1, -1):
    back = max(back, s[n - 2 - i] - 2 * a[n - 2 - i][0])
    ans = max(ans, t[i] - (c - a[n - i - 1][0]) + back)
print(ans)
