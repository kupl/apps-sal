import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W, N, *A = list(map(int, read().split()))

    C = [[0] * W for _ in range(H)]
    vec = [i for i, a in enumerate(A, 1) for _ in range(a)]

    for i in range(H):
        for j in range(W):
            color = vec[i * W + j]
            if i % 2 == 0:
                C[i][j] = color
            else:
                C[i][W - j - 1] = color

    for row in C:
        print((*row))

    return


def __starting_point():
    main()


__starting_point()
