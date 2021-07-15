n = int(input())
arr = [int(num) for num in input().strip().split()]
ans = 360
for i in range(n):
    l = 0
    r = 360
    for j in range(n):
        ans = min(ans, abs(l - r))
        l += arr[j]
        r -= arr[j]
    if ans == 0:
        break
    val = arr[0]
    arr.remove(arr[0])
    arr.append(val)
print(ans)
