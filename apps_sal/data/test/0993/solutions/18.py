import sys
from itertools import accumulate
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *A = list(map(int, read().split()))

    B = [0]
    B.extend(accumulate(A))
    B = [b % M for b in B]

    counter = Counter(B)
    ans = 0
    for v in list(counter.values()):
        ans += v * (v - 1) // 2

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
