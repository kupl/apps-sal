n = int(input())
arr = list(map(int, input().split()))
maxval = arr[0]
ans = 0
for i in range(n):
    maxval = max(arr[i], maxval)
    if(maxval == i + 1):
        ans += 1
        maxval = 0
print(ans)
