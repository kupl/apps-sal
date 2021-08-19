from collections import Counter
from typing import List


def answer(n: int, s: List[str]) -> List[str]:
    result = []
    judges = ['AC', 'WA', 'TLE', 'RE']
    aggregate = {i: 0 for i in judges}
    counter = Counter(s)
    for i in counter:
        aggregate[i] += counter[i]
    for j in aggregate:
        result.append(f'{j} x {aggregate[j]}')
    return result


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in answer(n, s):
        print(i)


def __starting_point():
    main()


__starting_point()
