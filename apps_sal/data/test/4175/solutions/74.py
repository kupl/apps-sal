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
ans = 'Yes'
N = ini()
words = []
for _ in range(N):
    words.append(input())
if len(words) != len(set(words)):
    ans = 'No'
for i in range(N - 1):
    if words[i][len(words[i]) - 1] != words[i + 1][0]:
        ans = 'No'
print(ans)
