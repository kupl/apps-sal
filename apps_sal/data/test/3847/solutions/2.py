import sys
from math import inf


def rint():
    return list(map(int, sys.stdin.readline().split()))


n, m = rint()

a = list(rint())
b = list(rint())
x = int(input())

asum = [0]
for i in range(n):
    asum.append(asum[-1] + a[i])

bsum = [0]
for i in range(m):
    bsum.append(bsum[-1] + b[i])

amin = [inf] * (n + 1)
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        partsum = asum[j] - asum[i]
        if amin[j - i] > partsum:
            amin[j - i] = partsum

bmin = [inf] * (m + 1)
for i in range(m + 1):
    for j in range(i + 1, m + 1):
        partsum = bsum[j] - bsum[i]
        if bmin[j - i] > partsum:
            bmin[j - i] = partsum

max_area = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if amin[i] * bmin[j] <= x and i * j > max_area:
            max_area = i * j

print(max_area)
