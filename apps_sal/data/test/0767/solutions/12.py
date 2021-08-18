
n, z = list(map(int, input().split()))

arr = list(map(int, input().split()))


arr.sort()
c = 0
l = 0
r = len(arr) // 2
while(r < len(arr) and l < len(arr)):
    if arr[l] == -1:
        l += 1
        continue
    if (arr[r] - arr[l]) >= z and arr[r] != -1:
        arr[r] = -1
        c += 1
        r += 1
        l += 1
    else:
        r += 1


print(c)
