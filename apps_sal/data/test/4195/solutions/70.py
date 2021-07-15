def main():
    d, n = list(map(int, input().split()))
    if d == 0:
        print(n + (n//100))
        return
    print((100 ** d) * (n + n // 100))


def __starting_point():
    main()
__starting_point()
