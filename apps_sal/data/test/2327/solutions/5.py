import sys
from collections import Counter
T = int(input().strip())
for t in range(T):
    n = int(input().strip())
    res = 0
    d = 1
    while n + 1 > d:
        res += ((n + 1) // d + (1 if (n + 1) % d else 0)) - 1
        d *= 2
    print(res)
