def main():
    (n, m) = [int(i) for i in input().split()]
    ans = []
    k = min(n, m) + 1
    print(k)
    for i in range(k):
        print(i, k - i - 1)


def __starting_point():
    main()


__starting_point()
