import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *X = list(map(int, read().split()))

    if N >= M:
        print((0))
        return

    X.sort()
    dist = [0] * (M - 1)
    for i in range(M - 1):
        dist[i] = X[i + 1] - X[i]

    dist.sort()
    ans = sum(dist[: M - N])

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
