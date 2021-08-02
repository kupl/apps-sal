import math
la, ra, ta = map(int, input().split())
lb, rb, tb = map(int, input().split())
x = math.gcd(ta, tb)
d = la - lb
print(max(min(ra - la + 1, rb - lb + 1 - d % x), min(rb - lb + 1, ra - la + 1 - (-d) % x), 0))
