import math
n = int(input())
arr = [int(x) for x in input().split()]
if n % 2 == 0:
    for i in range(len(arr)):
        if arr[i] >= 0:
            arr[i] = -arr[i] - 1
    for i in range(len(arr) - 1):
        print(arr[i], end=' ')
    print(arr[len(arr) - 1])
else:
    maxVal = arr[0]
    for i in range(n):
        if (maxVal + 0.5) ** 2 < (arr[i] + 0.5) ** 2:
            maxVal = arr[i]
    z = arr.index(maxVal)
    for i in range(len(arr)):
        if arr[i] >= 0:
            arr[i] = -arr[i] - 1
    arr[z] = -arr[z] - 1
    for i in range(len(arr) - 1):
        print(arr[i], end=' ')
    print(arr[len(arr) - 1])
