from typing import List


def answer(n: int, m: int, x: int, y: int, xs: List[int], ys: List[int]) -> str:
    xs.append(x)
    ys.append(y)
    if min(ys) <= max(xs):
        return 'War'
    return 'No War'


def main():
    (n, m, x, y) = list(map(int, input().split()))
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    print(answer(n, m, x, y, xs, ys))


def __starting_point():
    main()


__starting_point()
