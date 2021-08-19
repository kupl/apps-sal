import sys
import math
(n, x) = map(int, sys.stdin.readline().split())
xl = [*map(int, sys.stdin.readline().split())]
yl = [abs(x - i) for i in xl]
d = yl[0]
for i in range(n):
    d = math.gcd(d, yl[i])
print(d)
