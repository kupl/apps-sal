from math import sqrt


def main():
    N = int(input())
    ans = 1000000000000.0 + 1
    for i in range(1, int(sqrt(N)) + 1):
        if N % i == 0:
            j = N // i
            ans = min(ans, i + j - 2)
    print(ans)


def __starting_point():
    main()


__starting_point()
