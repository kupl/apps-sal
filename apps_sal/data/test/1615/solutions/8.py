def main():
    n, k = list(map(int, input().split()))
    res = 0
    for _ in range(n):
        a, b = list(map(int, input().split()))
        res -= b - a + 1
    print(res % k)


def __starting_point():
    main()


__starting_point()
