import sys

arr = [int(x) for x in input().split()]
n = arr[0]
m = arr[1]
k = arr[2]
if n % 2 != m % 2 and k == -1:
    print(0)
else:
    print(pow(2, (n - 1) * (m - 1), 1000 * 1000 * 1000 + 7))
