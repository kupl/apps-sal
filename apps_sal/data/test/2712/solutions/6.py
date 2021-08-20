import sys


def ii():
    return sys.stdin.readline().strip()


def idata():
    return [int(x) for x in ii().split()]


def solve():
    (a, b, c) = idata()
    print(max(a, b, c))
    return


for t in range(int(ii())):
    solve()
