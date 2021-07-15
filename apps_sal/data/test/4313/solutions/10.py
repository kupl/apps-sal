from typing import List


def answer(n: int, c: List[int], v: List[int]) -> int:
    return sum(list(j for j in (c[i] - v[i] for i in range(n)) if 0 < j))


def main():
    n = int(input())
    c = list(map(int, input().split()))
    v = list(map(int, input().split()))
    print(answer(n, c, v))


def __starting_point():
    main()
__starting_point()
