n, r, avg = list(map(int, input().split()))
a = [list(reversed(list(map(int, input().split())))) for i in range(n)]
a.sort()
cur = 0
req = avg * n
for i in range(n):
    cur += a[i][1]
i = 0
ans = 0
while i < n and cur < req:
    d = min(req - cur, r - a[i][1])
    ans += min(req - cur, r - a[i][1]) * a[i][0]
    i += 1
    cur += d
print(ans)
