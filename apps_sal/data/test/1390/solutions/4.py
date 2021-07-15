n, m = map(int, input().split())
arr = list(sorted(map(int, input().split())))
ans = arr[n - 1] - arr[0]
for i in range(1, m - n + 1):
    ans = min(ans, arr[i + n - 1] - arr[i])
print(ans)
