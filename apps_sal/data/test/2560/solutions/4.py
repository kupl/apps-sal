import sys
sys.setrecursionlimit(1000000)


def solve():
    (tests,) = rv()
    for test in range(tests):
        (n, l, r) = rv()
        largestused = (n + r - 1) // r
        totalnum = largestused * r
        mostcansubtract = largestused * (r - l)
        lowerbound = totalnum - mostcansubtract
        if lowerbound <= n:
            print('Yes')
        else:
            print('No')


def rv():
    return list(map(int, input().split()))


def rl(n):
    return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()
