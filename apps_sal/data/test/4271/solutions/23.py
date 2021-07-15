from typing import List


def answer(n: int, a: List[int], b: List[int], c: List[int]) -> int:
    satisfaction = sum(b)
    for i in range(1, n):
        previous = a[i - 1]
        if a[i] == previous + 1:
            satisfaction += c[previous - 1]

    return satisfaction


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print((answer(n, a, b, c)))


def __starting_point():
    main()

__starting_point()
