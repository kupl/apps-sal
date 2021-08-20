(n, x) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if a[i] + a[i - 1] > x:
        ans += min(a[i], a[i] + a[i - 1] - x)
        a[i] = max(0, x - a[i - 1])
    if a[i] + a[i - 1] > x:
        ans += a[i - 1] - x
        a[i - 1] = x
print(ans)
