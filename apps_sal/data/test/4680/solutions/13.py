from typing import List


def answer(abc: List[int]) -> str:
    return 'YES' if sorted(abc) == [5, 5, 7] else 'NO'


def main():
    abc = list(map(int, input().split()))
    print(answer(abc))


def __starting_point():
    main()
__starting_point()
