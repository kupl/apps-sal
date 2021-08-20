n = int(input())
arr = [int(x) for x in input().split()]
x = arr.index(max(arr))
cur = max(arr)
l = x - 1
r = x + 1
ok = 1
for i in range(n - 1):
    if l < 0:
        ok *= arr[r] < cur
        cur = arr[r]
        r += 1
    elif r >= n:
        ok *= arr[l] < cur
        cur = arr[l]
        l -= 1
    elif arr[l] > arr[r]:
        ok *= arr[l] < cur
        cur = arr[l]
        l -= 1
    else:
        ok *= arr[r] < cur
        cur = arr[r]
        r += 1
print('YES' if ok else 'NO')
