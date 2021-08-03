import sys
file = sys.stdin

__author__ = 'RaiaN'

n, m = file.readline().split(' ')
n = int(n)
m = int(m)
ms = [int(val) for val in file.readline().split(' ')]

dsb = [0] * n
for val in ms:
    for i in range(val - 1, n):
        if dsb[i] == 0:
            dsb[i] = val

print(' '.join(str(x) for x in dsb))
