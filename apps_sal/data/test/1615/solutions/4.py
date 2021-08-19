import sys
import math
(n, k) = [int(x) for x in sys.stdin.readline().split()]
vsum = 0
for i in range(n):
    (l, r) = [int(x) for x in sys.stdin.readline().split()]
    vsum += r - l + 1
if vsum % k == 0:
    print(0)
else:
    print(k - vsum % k)
