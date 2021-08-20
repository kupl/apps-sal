import sys
from typing import List


def answer(n: int, w: List[int]) -> int:
    w_left = 0
    w_right = sum(w)
    abs_of_difference = sys.maxsize
    for i in w:
        w_left += i
        w_right -= i
        abs_of_difference = min(abs_of_difference, abs(w_left - w_right))
    return abs_of_difference


def main():
    n = int(input())
    w = list(map(int, input().split()))
    print(answer(n, w))


def __starting_point():
    main()


__starting_point()
