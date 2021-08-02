from typing import List


def answer(n: int, a: List[int]) -> int:
    next_value = 1
    count = 0
    for _ in range(n):
        next_value = a[next_value - 1]
        count += 1
        if next_value == 2:
            return count

    return -1


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    print((answer(n, a)))


def __starting_point():
    main()


__starting_point()
