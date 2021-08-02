from itertools import accumulate
import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cumsum = list(accumulate([0] + A))
    ans = INF
    l = 0
    r = 2
    def fl(i, l): return abs(cumsum[i + 1] - 2 * cumsum[l + 1])
    def fr(i, r): return abs(cumsum[-1] - cumsum[i + 1] - 2 * (cumsum[r + 1] - cumsum[i + 1]))

    for i in range(1, N - 2):
        while fl(i, l + 1) < fl(i, l):
            l += 1
        while fr(i, r + 1) < fr(i, r):
            r += 1
        a = cumsum[l + 1]
        b = cumsum[i + 1] - a
        c = cumsum[r + 1] - a - b
        d = cumsum[-1] - a - b - c
        ans = min(ans, max(a, b, c, d) - min(a, b, c, d))
    print(ans)


def __starting_point():
    main()


__starting_point()
