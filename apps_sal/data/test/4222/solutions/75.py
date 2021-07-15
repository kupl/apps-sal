from typing import Union, List


def answer(n: int, k: int, da: List[Union[int, List[int]]]) -> int:
    result = set()
    for d, a in da:
        result |= set(a)

    return n - len(result)


def main():
    n, k = map(int, input().split())
    da = [[int(input()), list(map(int, input().split()))] for _ in range(k)]
    print(answer(n, k, da))


def __starting_point():
    main()
__starting_point()
