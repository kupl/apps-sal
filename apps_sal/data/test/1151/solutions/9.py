import bisect


n, u = list(map(int, input().split()))
ans = float(-1)
a = list(map(int, input().split()))
for i in range(0, n - 2, 1):
    x = int(bisect.bisect_left(a, a[i] + u + 1))
    x = x - 1
    if a[x] != a[i] and a[x] != a[i + 1]:
        ans = max(ans, (a[x] - a[i + 1]) * 1.0 / (a[x] - a[i]))
print(ans)
