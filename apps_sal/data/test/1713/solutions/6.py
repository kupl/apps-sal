import sys
import math
(n, s, t) = [int(x) for x in sys.stdin.readline().split()]
p = [int(x) for x in sys.stdin.readline().split()]
res = 0
k = s
while s != t and res < n:
    s = p[s - 1]
    res += 1
if t != s and res >= n:
    print(-1)
else:
    print(res)
