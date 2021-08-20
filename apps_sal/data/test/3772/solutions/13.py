def main():
    (a, b) = list(map(int, input().split()))
    res = 0
    while b:
        res += a // b
        (a, b) = (b, a % b)
    print(res)


def __starting_point():
    main()


__starting_point()
