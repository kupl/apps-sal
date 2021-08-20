from math import *
[n, k] = [int(i) for i in input().split()]
arr = [[0 for i in range(6)] for j in range(2)]
for i in [2, 3, 5]:
    while n % i == 0:
        n /= i
        arr[0][i] += 1
for i in [2, 3, 5]:
    while k % i == 0:
        k /= i
        arr[1][i] += 1
if n != k:
    print(-1)
else:
    r = abs(arr[1][5] - arr[0][5])
    r += abs(arr[1][3] - arr[0][3])
    r += abs(arr[1][2] - arr[0][2])
    print(r)
