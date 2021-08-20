(n, x) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
syaku = 0
for i in range(n - 1):
    if a[i] + a[i + 1] >= x:
        sa = a[i] + a[i + 1] - x
        ans += sa
        if sa <= a[i + 1]:
            a[i + 1] -= sa
        else:
            a[i] = sa - a[i + 1]
            a[i + 1] = 0
if n != 2 and a[n - 2] + a[n - 1] >= x:
    sa = a[i] + a[i + 1] - x
    ans += sa
    if sa <= a[n - 1]:
        a[n - 1] -= sa
    else:
        a[n - 2] = sa - a[n - 1]
        a[n - 1] = 0
print(ans)
