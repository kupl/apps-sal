import sys
from itertools import permutations


def answer(a: int, b: int, c: int, d: int, e: int) -> int:
    dishes = [a, b, c, d, e]
    ans = sys.maxsize

    for p in permutations(list(range(5))):
        result = 0
        for i in range(5):
            dish = dishes[p[i]]
            if i < 4:
                mod = dish % 10
                if mod != 0:
                    result += 10 - mod
            result += dish
        ans = min(ans, result)

    return ans


def main():
    a, b, c, d, e = (int(input()) for _ in range(5))
    print((answer(a, b, c, d, e)))


def __starting_point():
    main()


__starting_point()
