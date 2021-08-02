from typing import List


def answer(n: int, a: List[int]) -> int:
    height_sum = 0
    current_tallest = 0

    for i in a:
        if i < current_tallest:
            height_sum += current_tallest - i
        elif current_tallest < i:
            current_tallest = i

    return height_sum


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print((answer(n, a)))


def __starting_point():
    main()


__starting_point()
