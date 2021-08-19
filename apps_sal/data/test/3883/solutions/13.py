import sys
from math import sqrt
(x, y) = [int(x) for x in sys.stdin.readline().split()]
if y > x:
    print(-1)
else:
    s = (x + y) / 2
    r = (x - y) / 2
    ans = min(s / int(s / y), r / int(r / y)) if r >= y else s / int(s / y)
    print(ans)
