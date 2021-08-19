(n, x) = list(map(int, input().split()))
a = [int(y) for y in input().split()]
ans = 0
for i in range(1, n):
    d = a[i - 1] + a[i]
    if d <= x:
        continue
    a[i] -= min(a[i], d - x)
    a[i - 1] -= max(d - x - a[i], 0)
    ans += d - x
print(ans)
