def sum_of_digits(i: int) -> int:
    result = 0
    for _ in range(len(str(i))):
        i, mod = divmod(i, 10)
        result += mod

    return result


def answer(n: int, a: int, b: int) -> int:
    some_sums = 0
    for i in range(1, n + 1):
        if a <= sum_of_digits(i) <= b:
            some_sums += i

    return some_sums


def main():
    n, a, b = map(int, input().split())
    print(answer(n, a, b))


def __starting_point():
    main()


__starting_point()
