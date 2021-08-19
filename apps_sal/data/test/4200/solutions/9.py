from typing import List


def answer(n: int, m: int, a: List[int]) -> str:
    ref_value = sum(a) / (4 * m)
    result = len(list((i for i in a if ref_value <= i)))
    return 'Yes' if m <= result else 'No'


def main():
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    print(answer(n, m, a))


def __starting_point():
    main()


__starting_point()
