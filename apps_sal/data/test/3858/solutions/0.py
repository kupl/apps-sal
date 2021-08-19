from collections import Counter
from fractions import gcd
import sys
input = sys.stdin.readline
'\n適当に部分集合Xをとり、凸包 S として、Sに1点計上すればよい\nこれだと2^N点得られる\nただし、凸包の面積が0となる場合が例外\n空集合、1点の場合と、線分の場合を除外する\n\n'
MOD = 998244353
N = int(input())
XY = [[int(x) for x in input().split()] for _ in range(N)]
answer = pow(2, N, MOD)
answer -= N + 1
for (i, (x, y)) in enumerate(XY):
    pts = []
    for (x1, y1) in XY[i + 1:]:
        (dx, dy) = (x1 - x, y1 - y)
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        if dx < 0:
            (dx, dy) = (-dx, -dy)
        elif dx == 0:
            dy = 1
        pts.append((dx, dy))
    c = Counter(pts)
    for v in c.values():
        answer -= pow(2, v, MOD) - 1
answer %= MOD
print(answer)
