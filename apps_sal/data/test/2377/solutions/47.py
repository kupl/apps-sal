import sys
import numpy as np

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    N, H = inl()
    a = [None] * N
    b = [None] * N
    mi = None
    ma, mb = 0, 0
    for i in range(N):
        a[i], b[i] = inl()
        if a[i] > ma:
            mi = i
            ma = a[i]

    bm = max(b[mi], a[mi])
    am = a[mi]

    bb = []
    for i in range(N):
        bb.append((b[i], i))
    bb.sort(reverse=True)

    cnt = 0
    for i in range(N):
        if H <= 0:
            break
        x, j = bb[i]
        debug(H, x, j)
        if x < am:
            break
        H -= x
        cnt += 1
    if H > 0:
        k = (H + am - 1) // am
        cnt += k
        H -= k * am
        assert H <= 0

    return cnt


print(solve())
