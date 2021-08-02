from typing import List


def answer(n: int, d: int, xy: List[List[int]]) -> int:
    count = 0
    dd = d ** 2
    for x, y in xy:
        if x ** 2 + y ** 2 <= dd:
            count += 1

    return count


def main():
    n, d = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(n)]
    print((answer(n, d, xy)))


def __starting_point():
    main()


__starting_point()
