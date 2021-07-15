n = int(input())
arr = [int(x) for x in input().split()]
m = max(arr)
ans = 0
for x in arr:
    ans += m - x
print(ans)
