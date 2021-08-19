import sys
from functools import lru_cache
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, X) = list(map(int, readline().split()))

    @lru_cache(maxsize=None)
    def rec1(i):
        if i == 0:
            return 1
        else:
            return 2 * rec1(i - 1) + 1

    @lru_cache(maxsize=None)
    def rec2(i):
        if i == 0:
            return 1
        else:
            return 2 * rec2(i - 1) + 3

    def rec(i, x):
        if x <= 0:
            return 0
        if i == 0:
            return 1
        x -= 1
        ans = 0
        if x > rec2(i - 1):
            x -= rec2(i - 1)
            ans += rec1(i - 1)
        else:
            ans += rec(i - 1, x)
            return ans
        if x > 0:
            x -= 1
            ans += 1
        else:
            return ans
        if x > rec2(i - 1):
            x -= rec2(i - 1)
            ans += rec1(i - 1)
        else:
            ans += rec(i - 1, x)
        return ans
    print(rec(N, X))
    return


def __starting_point():
    main()


__starting_point()
