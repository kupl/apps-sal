from typing import List


def answer(n: int, k: int, p: List[int]) -> int:
    return sum(sorted(p)[:k])


def main():
    (n, k) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(answer(n, k, p))


def __starting_point():
    main()


__starting_point()
