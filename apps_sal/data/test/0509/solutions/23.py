import sys
from itertools import product

n = int(input())
a = [int(input()) for _ in range(n)]

for p in product([1, -1], repeat=n):
    tmp = 0
    for i, sgn in enumerate(p):
        tmp += sgn * a[i]
    if tmp % 360 == 0:
        print("YES")
        return
print("NO")
