import sys
import math
(n, m) = [int(x) for x in sys.stdin.readline().split()]
an = [int(x) for x in sys.stdin.readline().split()]
k = [0] * n
kj = [0] * 100001
k[n - 1] = 1
kj[an[n - 1]] = 1
for i in range(n - 2, -1, -1):
    z = 0
    if kj[an[i]] == 0:
        z = 1
    kj[an[i]] = 1
    k[i] = k[i + 1] + z
for i in range(m):
    d = int(sys.stdin.readline())
    print(k[d - 1])
