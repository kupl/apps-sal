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
ans = 'AC'
S = list(input())
if S.pop(0) != 'A':
    ans = 'WA'
if S.pop(0).isupper():
    ans = 'WA'
mid = S[0:-1]
if mid.count('C') == 1:
    mid.remove('C')
    for c in mid:
        if c.isupper():
            print(c)
            ans = 'WA'
else:
    ans = 'WA'
if S[-1].isupper():
    ans = 'WA'
print(ans)
