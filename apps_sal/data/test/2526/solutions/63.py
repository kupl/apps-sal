# ----------------
# ここから
# ----------------

import sys
from io import StringIO
import unittest
import heapq


def yn(b):
    print(("Yes" if b == 1 else "No"))
    return


def resolve():
    readline = sys.stdin.readline

    X, Y, a, b, c = list(map(int, readline().rstrip().split()))

    R = list([int(x) * (-1) for x in readline().rstrip().split()])
    G = list([int(x) * (-1) for x in readline().rstrip().split()])
    C = list([int(x) * (-1) for x in readline().rstrip().split()])

    heapq.heapify(R)
    heapq.heapify(G)
    heapq.heapify(C)
    ans = []
    heapq.heapify(ans)

    for _ in range(X):
        a = heapq.heappop(R)
        heapq.heappush(ans, a)
    for _ in range(Y):
        a = heapq.heappop(G)
        heapq.heappush(ans, a)
    for _ in range(min(X + Y, c)):
        a = heapq.heappop(C)
        heapq.heappush(ans, a)
    a = 0
    for _ in range(X + Y):
        a += heapq.heappop(ans) * -1

    print(a)
    # n=int(readline())
    # ss=readline().rstrip()
    # yn(1)

    return


if 'doTest' not in globals():
    resolve()
    return

# ----------------
# ここまで
# ----------------
