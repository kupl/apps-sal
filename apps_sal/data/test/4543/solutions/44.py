import math


def answer(a: int, b: int) -> str:
    joined_value = int(str(a) + str(b))
    return 'Yes' if math.sqrt(joined_value) % 1 == 0 else 'No'


def main():
    (a, b) = list(map(int, input().split()))
    print(answer(a, b))


def __starting_point():
    main()


__starting_point()
