n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = a[0] - 1
for i in range(1, m):
    if a[i] >= a[i - 1]:
        ans += a[i] - a[i - 1]
    else:
        ans += n - a[i - 1] + a[i]
print(ans)
