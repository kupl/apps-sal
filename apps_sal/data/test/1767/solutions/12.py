import itertools
import math
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
max1 = -1
for i in range(n):
    last_or_a = 0
    last_or_b = 0
    for j in range(i, n):
        last_or_a |= a[j]
        last_or_b |= b[j]
        max1 = max(max1, last_or_b + last_or_a)
print(max1)
