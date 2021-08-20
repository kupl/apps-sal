import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
T = int(stdin.readline())
for _ in range(T):
    (a, b, c, d) = list(map(int, stdin.readline().split()))
    if b >= a:
        print(b)
        continue
    rem = a - b
    if c - d <= 0:
        print(-1)
        continue
    ans = b + c * (rem // (c - d) + (1 if rem % (c - d) != 0 else 0))
    print(ans)
