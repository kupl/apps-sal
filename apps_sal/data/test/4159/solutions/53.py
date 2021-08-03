from typing import List


def answer(a: int, b: int, k: int) -> List[int]:
    if k <= a:
        a -= k
    elif k <= a + b:
        b -= k - a
        a = 0
    else:
        a = 0
        b = 0

    return [a, b]


def main():
    a, b, k = map(int, input().split())
    a, b = answer(a, b, k)
    print(a, b)


def __starting_point():
    main()


__starting_point()
