import sys


def input():
    return sys.stdin.readline().strip()


def mapint():
    return map(int, input().split())


sys.setrecursionlimit(10 ** 9)
N = int(input())
(l, r) = (0, 10 ** 18)
while l + 1 < r:
    half = (l + r) // 2
    if half * (half + 1) // 2 <= N + 1:
        l = half
    else:
        r = half
print(N + 1 - l)
