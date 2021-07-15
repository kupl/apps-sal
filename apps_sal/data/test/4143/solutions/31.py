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
    for i in range(5):
        res = (N + A[i] - 1) // A[i] + 4
        if ans < res:
            ans = res

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
