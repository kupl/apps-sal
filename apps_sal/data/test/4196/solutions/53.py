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
    vec1 = list(accumulate(A, func=gcd))
    vec2 = list(accumulate(reversed(A), func=gcd))
    ans = 0
    for i in range(N):
        if i == 0:
            res = vec2[-2]
        elif i == N - 1:
            res = vec1[-2]
        else:
            res = gcd(vec1[i - 1], vec2[N - i - 2])
        if ans < res:
            ans = res
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
