def answer(x: int) -> int:
    if x < 4 :
        return 1

    result = 1
    for b in range(2, x + 1):
        for p in range(2, x + 1):
            exp = pow(b, p)
            if exp <= x:
                result = max(result, exp)
            else:
                break

    return result


def main():
    x = int(input())
    print((answer(x)))


def __starting_point():
    main()

__starting_point()
