(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
arr = list()
for i in range(n):
    arr.append(((10 - a[i] + a[i] // 10 * 10) % 10, a[i]))
arr.sort()
ans = 0
for i in range(n):
    if arr[i][1] >= 100 or k - arr[i][0] < 0:
        ans += arr[i][1] // 10
        continue
    k -= arr[i][0]
    ans += (arr[i][1] + arr[i][0]) // 10
t = 10 * n - ans
ans += min(k // 10, t)
print(ans)
