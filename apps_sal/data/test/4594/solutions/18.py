from typing import List


def answer(n: int, d: List[int]) -> int:
    return len(set(d))


def main():
    n = int(input())
    d = list(int(input()) for _ in range(n))
    print(answer(n, d))


def __starting_point():
    main()


__starting_point()
