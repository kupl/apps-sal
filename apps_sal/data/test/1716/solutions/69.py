import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N, M, Q = list(map(int, readline().split()))
    A = [[0] * N for _ in range(N)]
    for _ in range(M):
        l, r = list(map(int, readline().split()))
        A[l - 1][r - 1] += 1

    B = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            B[i + 1][j + 1] = B[i][j + 1] + B[i + 1][j] - B[i][j] + A[i][j]

    ans = [0] * Q
    for i in range(Q):
        p, q = list(map(int, readline().split()))
        p -= 1
        q -= 1
        ans[i] = B[q + 1][q + 1] - B[q + 1][p] - B[p][q + 1] + B[p][p]

    print(('\n'.join(map(str, ans))))
    return


def __starting_point():
    main()


__starting_point()
