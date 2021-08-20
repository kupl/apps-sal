from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10 ** 20
MOD = 10 ** 9 + 7


def I():
    return list(map(int, input().split()))


def solve():
    (n,) = I()
    a = I()
    count = [0, 0, 0]
    for i in range(n):
        if i % 2 == a[i] % 2:
            continue
        count[a[i] % 2] += 1
    if count[0] != count[1]:
        print(-1)
    else:
        print(count[0])


(t,) = I()
while t:
    t -= 1
    solve()
