from typing import List


def judge(c: int, m: int, b: List[int], a: List[int]) -> bool:
    result = c
    for i in range(m):
        result += a[i] * b[i]

    return 0 < result


def answer(n: int, m: int, c: int, b: List[int], a: List[List[int]]) -> int:
    count = 0
    for i in range(n):
        if judge(c, m, b, a[i]):
            count += 1

    return count


def main():
    n, m, c = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]

    print((answer(n, m, c, b, a)))


def __starting_point():
    main()


__starting_point()
