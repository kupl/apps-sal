from typing import List


def next_coordinates(d: int, l: int) -> int:
    return d + l


def answer(n: int, x: int, l: List[int]) -> int:
    d = 0
    count = 1
    for i in l:
        d = next_coordinates(d, i)
        if x < d:
            return count
        count += 1
    return count


def main():
    (n, x) = map(int, input().split())
    l = list(map(int, input().split()))
    print(answer(n, x, l))


def __starting_point():
    main()


__starting_point()
