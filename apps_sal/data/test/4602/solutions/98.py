from typing import List


def answer(n: int, k: int, xs: List[int]) -> int:
    moving_distance = 0
    reference_value = k / 2
    for x in xs:
        if x <= reference_value:
            moving_distance += x * 2
        else:
            moving_distance += (k - x) * 2

    return moving_distance


def main():
    n = int(input())
    k = int(input())
    xs = list(map(int, input().split()))
    print(answer(n, k, xs))


def __starting_point():
    main()


__starting_point()
