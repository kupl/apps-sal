from itertools import combinations
from typing import List


def answer(n: int, d: List[int]) -> int:
    return sum((d[x] * d[y] for (x, y) in combinations(list(range(n)), 2)))


def main():
    n = int(input())
    d = list(map(int, input().split()))
    print(answer(n, d))


def __starting_point():
    main()


__starting_point()
