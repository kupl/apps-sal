from typing import List


def answer(n: int, h: List[int]) -> int:
    count = 0
    highest = 0
    for mountain in h:
        if highest <= mountain:
            highest = mountain
            count += 1
    return count


def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(answer(n, h))


def __starting_point():
    main()


__starting_point()
