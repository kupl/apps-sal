import math
import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def solve(N, A, EPS=1e-3):
    D = [A[i] - i - 1 for i in range(N)]
    D.sort()
    if N == 1:
        median = sum([abs(d - D[0]) for d in D])
        return median
    median_left = sum([abs(d - D[N // 2]) for d in D])
    median_right = sum([abs(d - D[N // 2 + 1]) for d in D])
    return min(median_left, median_right)


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print(("%s" % str(outputs)))


__starting_point()
