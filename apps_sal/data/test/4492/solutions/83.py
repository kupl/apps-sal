(N, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    if a[i] + a[i + 1] > x:
        diff = a[i] + a[i + 1] - x
        ans += diff
        a[i + 1] -= min(diff, a[i + 1])
print(ans)
