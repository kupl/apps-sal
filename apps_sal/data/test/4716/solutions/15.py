from typing import List


def answer(n: int, k: int, l: List[int]) -> int:
    l.sort(reverse=True)
    return sum(l[:k])


def main():
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    print((answer(n, k, l)))


def __starting_point():
    main()


__starting_point()
