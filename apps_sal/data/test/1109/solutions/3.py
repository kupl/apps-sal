from math import *

[n, k] = [int(i) for i in input().split()]
arr = [int(i) - 1 for i in input().split()]
arr2 = [[0 for i in range(2)] for j in range(k)]
r = 0
for i in range(n // k):
    for j in range(k):
        arr2[j][arr[i * k + j]] += 1
for j in range(k):
    r += min(arr2[j][0], arr2[j][1])
print(r)

