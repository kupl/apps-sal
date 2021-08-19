# coding: utf-8


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]

    for i in range(1, N):
        A[0][i] += A[0][i - 1]
        A[1][N - i - 1] += A[1][N - i]

    ans = max([A[0][i] + A[1][i] for i in range(N)])

    print(ans)


def __starting_point():
    main()


__starting_point()
