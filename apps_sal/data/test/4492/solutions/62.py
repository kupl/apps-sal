(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
if a[0] > x:
    ans += a[0] - x
    a[0] = x
for i in range(n - 1):
    if a[i] + a[i + 1] > x:
        if a[i + 1] > x - a[i]:
            ans += a[i + 1] - (x - a[i])
            a[i + 1] = x - a[i]
if a[-2] + a[i - 1] > x:
    if a[-1] > x - a[-2]:
        ans += a[-1] - (x - a[-2])
        a[-1] = x - a[-2]
print(ans)
