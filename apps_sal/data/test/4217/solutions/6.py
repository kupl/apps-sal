from collections import Counter
from typing import List


def answer(n: int, m: int, kas: List[List[int]]) -> int:
    response = sum((ka[1:] for ka in kas), [])
    result = list(Counter(response).values())
    return result.count(n)


def main():
    n, m = map(int, input().split())
    kas = [list(map(int, input().split())) for _ in range(n)]
    print(answer(n, m, kas))


def __starting_point():
    main()


__starting_point()
