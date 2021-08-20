from itertools import combinations
from typing import List


def answer(n: int, l: List[int]) -> int:
    count = 0
    l.sort()
    for (i, j, k) in combinations(l, 3):
        if i != j != k and k < i + j:
            count += 1
    return count


def main():
    n = int(input())
    l = list(map(int, input().split()))
    print(answer(n, l))


def __starting_point():
    main()


__starting_point()
