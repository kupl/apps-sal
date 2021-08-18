import math
import sys
sys.setrecursionlimit(10 ** 8)
def getnum(t=int): return t(sys.stdin.buffer.readline())
def numline(t=int): return list(map(t, sys.stdin.buffer.readline().split()))
def numread(t=int): return list(map(t, sys.stdin.buffer.read().split()))
def getstr(): return sys.stdin.readline().strip()
def strline(): return sys.stdin.readline().strip().split()
def strread(): return sys.stdin.read().strip().split()


mod = 998_244_353


def fromleft(N):
    for i in range(1, N):
        print((i, i + 1))


def fromright(N):
    for i in range(N, 1, -1):
        print((i, i - 1))


def main():
    N, *A = numread()
    A = [(a, i) for i, a in enumerate(A, 1)]
    (minA, mini), (maxA, maxi) = min(A, key=lambda x: x[0]), max(A, key=lambda x: x[0])
    if minA > 0:
        print((N - 1))
        fromleft(N)
        return
    elif maxA <= 0:
        print((N - 1))
        fromright(N)
        return
    elif abs(minA) > abs(maxA):
        print((2 * N - 1))
        for i in range(1, N + 1):
            print((mini, i))
        fromright(N)
        return
    else:
        print((2 * N - 1))
        for i in range(1, N + 1):
            print((maxi, i))
        fromleft(N)
        return


def __starting_point():
    main()


__starting_point()
