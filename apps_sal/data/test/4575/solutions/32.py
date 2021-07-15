from typing import List


def answer(n: int, d: int, x: int, a: List[int]) -> int:
    eaten_chocolates = 0
    for i in range(n):
        eaten_chocolates += len(list(range(1, d + 1, a[i])))

    return eaten_chocolates + x


def main():
    n = int(input())
    d, x = list(map(int, input().split()))
    a = [int(input()) for _ in range(n)]
    print((answer(n, d, x, a)))


def __starting_point():
    main()

__starting_point()
