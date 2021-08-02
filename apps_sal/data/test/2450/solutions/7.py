from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10**20
MOD = 10**9 + 7
I = lambda: list(map(int, input().split()))


def solve():
    n, m, x, y = I()
    ans = 0
    for i in range(n):
        s = input()
        count = 0
        for j in range(m):
            if s[j] == '.':
                count += 1
            else:
                ans += min(x * count, count // 2 * y + (count % 2) * x)
                count = 0
        ans += min(x * count, count // 2 * y + (count % 2) * x)
    print(ans)


t, = I()
while t:
    t -= 1
    solve()
