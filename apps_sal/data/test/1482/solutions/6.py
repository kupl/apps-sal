import sys
import math
(n, k) = [int(x) for x in sys.stdin.readline().split()]
an = [int(x) for x in sys.stdin.readline().split()]
k = [0] * (n * k)
for i in an:
    k[i - 1] = 1
j = 0
for i in an:
    v = []
    count = 0
    while count != n - 1:
        if k[j] != 1:
            v.append(str(j + 1))
            count += 1
        j += 1
    v.append(str(i))
    print(' '.join(v))
