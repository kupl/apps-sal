n = int(input())
arr = [int(x) for x in input().split()]
prev = arr[0]
ans = 1
c = 1
for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        c += 1
    else:
        c = 1
    ans = max(ans, c)
print(ans)
