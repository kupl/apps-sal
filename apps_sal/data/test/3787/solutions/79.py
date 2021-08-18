import sys
import collections
import itertools

sys.setrecursionlimit(10 ** 8)
def inm(): return list(map(int, sys.stdin.readline().split()))


N, A, B = inm()


def solve():
    if A + B > N + 1:
        return None
    a, b = N, 1
    b += B - 1
    a -= B - 1

    s = []
    s.append(list(range(B, 0, -1)))
    la = 1
    p = B + 1
    ra = N - p + 1
    while la + ra > A:
        p2 = p + min(B, la + ra - A + 1)
        s.append(list(range(p2 - 1, p - 1, -1)))
        p = p2
        la += 1
        ra = N + 1 - p
        if la == A and ra > 0:
            return None
    assert la + ra == A
    s.append(list(range(p, N + 1)))
    return list(itertools.chain.from_iterable(s))


ans = solve()
if ans is None:
    print((-1))
else:
    print((*ans))
