from typing import List


def answer(n: int, s: List[str]) -> List[str]:
    result = []
    judges = ['AC', 'WA', 'TLE', 'RE']
    for i in judges:
        result.append(f'{i} x {s.count(i)}')

    return result


def main():
    n, *s = open(0).read().split()
    for i in answer(n, s):
        print(i)


def __starting_point():
    main()


__starting_point()
