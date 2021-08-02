n = int(input())
arr = list(map(int, input().split()))
ans = arr[-1]
val = max(arr[-1] - 1, 0)
for i in range(n - 2, -1, -1):
    if(arr[i] > val):
        ans += val
        val = max(val - 1, 0)
    else:
        ans += arr[i]
        val = max(arr[i] - 1, 0)
print(ans)
