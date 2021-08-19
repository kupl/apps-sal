(n, x) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    if a[i] <= x:
        if a[i] + a[i + 1] <= x:
            continue
        else:
            ans += a[i] + a[i + 1] - x
            a[i + 1] -= a[i] + a[i + 1] - x
    else:
        ans += a[i] - x + a[i + 1]
        (a[i], a[i + 1]) = (x, 0)
if a[-1] > x:
    ans += a[-1] - x
print(ans)
