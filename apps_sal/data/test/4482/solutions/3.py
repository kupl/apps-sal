from typing import List


def answer(n: int, a: List[int]) -> int:
    cost = 0
    num = round(sum(a) / n)
    for i in a:
        cost += (i - num) ** 2

    return cost


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(n, a))


def __starting_point():
    main()


__starting_point()
