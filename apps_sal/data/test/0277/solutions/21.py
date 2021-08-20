import sys
import itertools as it
import math
(n, a, b) = list(map(int, sys.stdin.readline().split()))
a -= 1
b -= 1
logn = int(math.log2(n))
for k in range(logn):
    if a & 1 << logn - k - 1 != b & 1 << logn - k - 1:
        if k == 0:
            print('Final!')
        else:
            print(logn - k)
        break
