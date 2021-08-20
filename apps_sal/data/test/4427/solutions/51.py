from typing import List


def answer(r: int, d: int, x: int) -> List[int]:
    result = []
    for _ in range(10):
        x = r * x - d
        result.append(x)
    return result


def main():
    (r, x, d) = list(map(int, input().split()))
    for i in answer(r, x, d):
        print(i)


def __starting_point():
    main()


__starting_point()
