import sys
input = sys.stdin.readline
import math


def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def find_minimum(N, A, l, r):
    """閉区間[l, r]の最小値を返す"""
    m = (r + 2 * l) // 3
    q = (2 * r + l) // 3
    lf = sum([abs(A[i] - l) for i in range(N)])
    rf = sum([abs(A[i] - r) for i in range(N)])
    mf = sum([abs(A[i] - m) for i in range(N)])
    qf = sum([abs(A[i] - q) for i in range(N)])
    while r - l >= 3:
        m = (r + 2 * l) // 3
        q = (2 * r + l) // 3
        lf = sum([abs(A[i] - l) for i in range(N)])
        mf = sum([abs(A[i] - m) for i in range(N)])
        qf = sum([abs(A[i] - q) for i in range(N)])
        rf = sum([abs(A[i] - r) for i in range(N)])
        if mf >= qf:
            l = m
        else:
            r = q
    return min(lf, mf, qf, rf)


def solve(N, A, EPS=1e-3):
    D = [A[i] - i - 1 for i in range(N)]
    return find_minimum(N, D, l=-10**10, r=10**10)


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print(("%s" % str(outputs)))

__starting_point()
