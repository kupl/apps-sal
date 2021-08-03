N, x = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
keep = a[0]
for i in range(1, N):
    if (keep + a[i]) > x:
        ans = ans + (keep + a[i] - x)
        keep = max(x - keep, 0)
    else:
        keep = a[i]


print(ans)
