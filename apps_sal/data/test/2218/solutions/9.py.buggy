from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys


def fastio():
    from io import StringIO
    from atexit import register
    nonlocal input
    sys.stdin = StringIO(sys.stdin.read())
    def input(): return sys.stdin.readline().rstrip('\r\n')
    sys.stdout = StringIO()
    register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


fastio()


def debug(*var, sep=' ', end='\n'):
    print(*var, file=sys.stderr, end=end, sep=sep)


INF = 10**20
MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


n, k = I()
a = I()
a.sort(reverse=1)

p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] += p[i - 1] + a[i - 1]

s = set()
window = 1
ans = []
while k and window <= n:
    for i in range(window, n + 1):
        print(window, *ans, a[i - 1])
        k -= 1
        if not k:
            break
    ans.append(a[window - 1])
    window += 1
