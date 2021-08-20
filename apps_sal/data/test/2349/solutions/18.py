from bisect import bisect_right
from bisect import bisect_left
from collections import defaultdict
from math import sqrt, factorial, gcd, log2, inf, ceil
import sys
t = int(input())
for _ in range(t):
    n = int(input())
    ans = [1, 0]
    for i in range(1, int(sqrt(n) + 1)):
        ans.append(n // i)
        ans.append(n // (n // i))
    ans = list(set(ans))
    print(len(ans))
    ans.sort()
    print(*ans)
