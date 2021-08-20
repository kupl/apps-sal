n = int(input())
arr = [int(x) for x in input().split()]
M = max(arr)
m = min(arr)
cnt = 0
for i in arr:
    if i > m and i < M:
        cnt += 1
print(cnt)
