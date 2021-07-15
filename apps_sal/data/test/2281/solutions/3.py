import collections
import math

n  = int(input())
arr = [0] * (2 * n)
l, r = 0, 0
for i in range(1, n):
    if i % 2 == 1:
        arr[l] = arr[l + n - i] = i
        l += 1
    else:
        arr[n + r] = arr[n + r + n - i] = i
        r += 1
for i in range(2):
    while arr[l]:
        l += 1
    arr[l] = n
print(' '.join(str(x) for x in arr))
