import sys


def ii():
    return sys.stdin.readline().strip()


def idata():
    return [int(x) for x in ii().split()]


def solve():
    n = int(ii())
    data = idata()
    print(*data[::-1])
    return


for t in range(int(ii())):
    solve()
