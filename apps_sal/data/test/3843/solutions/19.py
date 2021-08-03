import sys
import math
from itertools import permutations


def convert(n):
    if n == 0:
        return []
    return convert(n // 7) + [n % 7]


n, m = list(map(int, sys.stdin.readline().split()))
x = convert(n - 1)
y = convert(m - 1)
nn = max(1, len(x))
mm = max(1, len(y))
ans = 0
for i in permutations("0123456", nn + mm):
    a, b = "".join(i[:nn]), "".join(i[nn:])
    ans += (int(a, 7) < n and int(b, 7) < m)
sys.stdout.write(str(ans))
