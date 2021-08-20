import math
import sys
sys.setrecursionlimit(1000000)


def solve():
    (n,) = rv()
    l = list()
    already = [-1] * (2 * n)
    for i in range(2 * n - 1):
        (temp,) = rl(1)
        for (j, val) in enumerate(temp):
            l.append((val, i + 1, j))
    l.sort(key=lambda x: -x[0])
    for tup in l:
        (f, s) = (tup[1], tup[2])
        if already[f] == -1 and already[s] == -1:
            already[f] = s
            already[s] = f
    print(' '.join(map(str, [val + 1 for val in already])))


def rv():
    return list(map(int, input().split()))


def rl(n):
    return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()
