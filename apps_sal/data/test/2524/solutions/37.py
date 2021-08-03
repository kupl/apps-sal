import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, read().split()))

    ans = 0
    for i in range(60):
        one = 0
        for a in A:
            if a & (1 << i):
                one += 1
        ans = (ans + one * (N - one) * (1 << i)) % MOD

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
