#!/user/bin/env pypy3
import sys
from functools import reduce


def fast_input():
    return sys.stdin.readline()[:-1]


def digit_sum(num: int) -> int:
    str_num = str(num)
    return reduce(
        lambda acc, n: acc + int(n),
        list(str_num),
        0
    )


def solve(n: int, a: int, b: int) -> int:
    num_sum = 0
    for num in range(1, n + 1):
        if a <= digit_sum(num) <= b:
            num_sum += num
    return num_sum


def main():
    [n, a, b] = list(map(int, fast_input().split()))
    result = solve(n, a, b)
    print(result)


main()
