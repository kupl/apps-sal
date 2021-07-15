n = int(input())
arr = [int(x) for x in input().split()]

ans = 1
now = 1
for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        now += 1
    else:
        ans = max(ans, now)
        now = 1
        
ans = max(ans, now)
print(ans)
