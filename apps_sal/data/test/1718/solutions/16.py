
def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    n = n - 1
    k = k - 1
    print((n // k if n % k == 0 else (n // k + 1)))


def __starting_point():
    main()


__starting_point()
