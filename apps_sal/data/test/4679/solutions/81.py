import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)


def ini():
    return int(sys.stdin.readline())


def inl():
    return [int(x) for x in sys.stdin.readline().split()]


def ins():
    return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print('\x1b[33m', *a, '\x1b[0m', **dict(file=sys.stderr, **kw))


def solve():
    S = [deque(ins()) for _ in range(3)]
    abc = {'a': 0, 'b': 1, 'c': 2}
    i = 0
    while True:
        if not S[i]:
            return i
        x = S[i].popleft()
        i = abc[x]
    return


print('ABC'[solve()])
