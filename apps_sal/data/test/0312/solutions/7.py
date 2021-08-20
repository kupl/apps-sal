import sys
sys.setrecursionlimit(1000000)


def solve():
    (n, m) = rv()
    if n == 1:
        return 1
    toleft = m - 1
    toright = n - m
    if toleft >= toright:
        return m - 1
    return m + 1


def rv():
    return list(map(int, input().split()))


def rl(n):
    return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
print(solve())
