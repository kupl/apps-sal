import sys
import math
sys.setrecursionlimit(10 ** 8)


def ini():
    return int(sys.stdin.readline())


def inm():
    return map(int, sys.stdin.readline().split())


def inl():
    return list(inm())


def ins():
    return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print('\x1b[33m', *a, '\x1b[0m', **dict(file=sys.stderr, **kw))
tasks = inl()
tasks.sort()
ans = 0
for i in range(len(tasks) - 1):
    ans += tasks[i + 1] - tasks[i]
print(ans)
