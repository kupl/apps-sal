n = int(input())
arr = list(map(int, input().split()))
(ans, cursum) = (0, 0)
arr.sort()
for i in range(n):
    cursum += arr[i]
for i in range(n):
    ans += cursum
    if i < n - 1:
        ans += arr[i]
    cursum -= arr[i]
print(ans)
