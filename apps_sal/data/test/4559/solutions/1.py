from typing import List


def answer(n: int, a: List[int]) -> int:
    if 0 in a:
        return 0

    max_value = 10 ** 18
    product = 1
    for i in a:
        product *= i
        if max_value < product:
            return -1

    return product


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(n, a))


def __starting_point():
    main()
__starting_point()
