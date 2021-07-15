# coding: utf-8


def main():
    N, K = list(map(int, input().split()))
    ans = 0 if (N - 1) % (K - 1) == 0 else 1
    ans += (N - 1) // (K - 1)
    print(ans)


def __starting_point():
    main()

__starting_point()
