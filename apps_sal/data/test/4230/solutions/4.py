from typing import List


def answer(x: int, n: int, p: List[int]) -> int:
    not_included = set(range(0, 102)).difference(p)
    return sorted(not_included, key=lambda i: abs(i - x))[0]


def main():
    x, n = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print((answer(x, n, p)))


def __starting_point():
    main()


__starting_point()
