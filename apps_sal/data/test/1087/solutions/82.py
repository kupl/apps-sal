import sys
from functools import lru_cache

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *A = list(map(int, read().split()))

    counter = [0] * 40
    for a in A:
        for i in range(40):
            if a & (1 << i):
                counter[i] += 1

    Y = 0
    for i in range(39, -1, -1):
        Y <<= 1
        if counter[i] < N - counter[i]:
            Y += 1

    ans = 0
    for a in A:
        ans += K ^ a
    for i in range(40):
        if K & (1 << i):
            x = ((K >> (i + 1)) << (i + 1)) + Y % (1 << i)
            res = 0
            for a in A:
                res += x ^ a
            if ans < res:
                ans = res

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
