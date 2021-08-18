import os
import sys

n, m = [int(num) for num in sys.stdin.readline().split()]


res1 = max([0, n - 2 * m])
res2 = 0
while res2 * (res2 - 1) < (2 * m):
    res2 += 1

print(res1, n - res2)
