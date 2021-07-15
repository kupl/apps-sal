import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    def rec(n, used):
        ans = 0
        if all(used):
            ans += 1
        for i, d in enumerate((3, 7, 5)):
            if 10 * n + d <= N:
                cur = used[i]
                used[i] = True
                ans += rec(10 * n + d, used)
                used[i] = cur
        return ans

    print((rec(0, [False, False, False])))
    return


def __starting_point():
    main()

__starting_point()
