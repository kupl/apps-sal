import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, read().split()))

    dp_used = [[-INF] * 2 for _ in range(N + 1)]
    dp_unused = [[-INF] * 2 for _ in range(N + 1)]

    dp_used[0][1] = dp_unused[0][1] = 0

    for i in range(N):
        if i % 2 == 0:
            dp_unused[i + 1][0] = max(dp_used[i][1], dp_unused[i][1])
            dp_used[i + 1][0] = dp_unused[i][0] + A[i]
            dp_used[i + 1][1] = dp_unused[i][1] + A[i]
        else:
            dp_unused[i + 1][0] = max(dp_unused[i][0], dp_used[i][0])
            dp_unused[i + 1][1] = dp_used[i][1]
            dp_used[i + 1][1] = dp_unused[i][0] + A[i]

    if N % 2 == 0:
        print((max(dp_unused[N][1], dp_used[N][1])))
    else:
        print((max(dp_unused[N][0], dp_used[N][0])))

    return


def __starting_point():
    main()

__starting_point()
