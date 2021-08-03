from typing import List


def answer(n: int, p: List[int]) -> str:
    count = 0
    for i, num in enumerate(p, start=1):
        if i != num:
            count += 1

    return 'YES' if count <= 2 else 'NO'


def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(answer(n, p))


def __starting_point():
    main()


__starting_point()
