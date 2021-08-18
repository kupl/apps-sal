import functools
from bisect import bisect_left
arr = []
brr = []
n, m = list(map(int, input().split()))
for i in range(n):
    x, u = list(map(int, input().split()))
    arr.append((x * u, x))
arr.sort()
arr = [a[0] for a in arr]
for i in range(m):
    y, v = list(map(int, input().split()))
    brr.append((y, y * v))
brr.sort()
brr = [a[1] for a in brr]
count = 0
for i in range(m):
    pos = bisect_left(arr, brr[i])
    if pos < len(arr) and arr[pos] == brr[i]:
        count += 1
        arr.pop(pos)

print(count)
