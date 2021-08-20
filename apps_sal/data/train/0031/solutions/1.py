from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10 ** 20
MOD = 10 ** 9 + 7


def I():
    return list(map(int, input().split()))


(t,) = I()
while t:
    t -= 1
    s = input()
    (x, y) = (0, 0)
    d = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
    ans = 0
    v = dd(int)
    for i in s:
        (a, b) = (x + d[i][0], y + d[i][1])
        if (x, y, a, b) in v:
            ans += 1
        else:
            ans += 5
        v[x, y, a, b] = v[a, b, x, y] = 1
        (x, y) = (a, b)
    print(ans)
