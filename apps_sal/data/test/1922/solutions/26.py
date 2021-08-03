# coding: utf-8


def main():
    N, M = list(map(int, input().split()))
    if N == 1 or M == 1:
        ans = N * M - 2
        if ans < 0:
            ans = 1
    else:
        ans = N * M - (N + M) * 2 + 4

    print(ans)


def __starting_point():
    main()


__starting_point()
