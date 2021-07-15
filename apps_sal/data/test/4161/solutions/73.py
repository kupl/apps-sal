from math import gcd


def answer(k: int) -> int:
    result = 0
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            temp = gcd(a, b)
            for c in range(1, k + 1):
                result += gcd(temp, c)

    return result


def main():
    k = int(input())
    print((answer(k)))


def __starting_point():
    main()

__starting_point()
