def f(n):
    if n % 2 == 0:
        return (n // 2)
    return (-n + n // 2)


def main():
    n = int(input())
    print(f(n))


def __starting_point():
    main()


__starting_point()
