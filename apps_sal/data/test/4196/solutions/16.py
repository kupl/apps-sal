import sys
from math import gcd
from itertools import accumulate
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, *A) = list(map(int, read().split()))
    vec1 = [0] * (N + 1)
    vec2 = [0] * (N + 1)
    for i in range(N):
        vec1[i + 1] = gcd(vec1[i], A[i])
    for i in range(N - 1, -1, -1):
        vec2[i] = gcd(vec2[i + 1], A[i])
    ans = 0
    for i in range(N):
        g = gcd(vec1[i], vec2[i + 1])
        if ans < g:
            ans = g
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
