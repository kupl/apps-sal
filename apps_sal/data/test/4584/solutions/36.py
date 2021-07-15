from typing import List


def answer(n: int, a: List[int]) -> List[int]:
    result = [0] * n
    for i in a:
        result[i - 1] += 1
    return result


def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in answer(n, a):
        print(i)


def __starting_point():
    main()
__starting_point()
