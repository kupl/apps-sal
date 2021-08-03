import sys
import math

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    a, b, c, d = inl()
    cd = c * d // math.gcd(c, d)
    r1 = b // c + b // d - b // cd
    r2 = (a - 1) // c + (a - 1) // d - (a - 1) // cd
    ans = (b - r1) - (a - 1 - r2)
    return ans


print(solve())
