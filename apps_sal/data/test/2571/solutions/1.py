import sys


def ii():
    return sys.stdin.readline().strip()


def idata():
    return [int(qw) for qw in ii().split()]


mod = 998244353


def solve():
    n = int(ii())
    data = idata()
    for i in range(0, n, 2):
        (data[i], data[i + 1]) = (-data[i + 1], data[i])
    print(*data)
    return


for _t in range(int(ii())):
    solve()
