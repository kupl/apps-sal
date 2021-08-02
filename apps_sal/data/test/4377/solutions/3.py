arr = list(map(int, input().split()))
arr.sort()
ans = []
for i in range(3):
    ans.append(arr[-1] - arr[i])
print(*ans)
