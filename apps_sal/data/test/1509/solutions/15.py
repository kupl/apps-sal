n = int(input())
arr = list(map(int, input().split()))
ans = 0
ans += arr[0] * (n - arr[0] + 1)
for i in range(1, n):
    if arr[i - 1] < arr[i]:
        ans += (arr[i] - arr[i - 1]) * (n - arr[i] + 1)
    if arr[i - 1] > arr[i]:
        ans += arr[i] * (arr[i - 1] - arr[i])
print(ans)
