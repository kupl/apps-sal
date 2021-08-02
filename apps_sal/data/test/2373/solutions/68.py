n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    if arr[i] == i + 1:
        ans += 1
        arr[i + 1], arr[i] = arr[i], arr[i + 1]
if arr[n - 1] == n:
    ans += 1
print(ans)
