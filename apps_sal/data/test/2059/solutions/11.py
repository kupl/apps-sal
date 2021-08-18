

import math

n = int(input())

a = list(map(int, input().split()))

k = math.inf
for i in range(n):
    if k > a[i] // max(n - i - 1, i):
        k = a[i] // max(n - i - 1, i)
print(k)
