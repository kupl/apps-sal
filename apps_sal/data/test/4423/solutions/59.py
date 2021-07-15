from typing import List, Tuple


def answer(n: int, sps: List[Tuple[str, int]]) -> List[int]:
    result = []
    numbered_sps = []
    for i, sp in enumerate(sps, start=1):
        s, p = sp
        numbered_sps.append([i, s, p])
    numbered_sps = sorted(numbered_sps, key=lambda x: (x[1], -x[2]))
    for i in numbered_sps:
        result.append(i[0])

    return result


def main():
    n = int(input())
    temp = (input().split() for _ in range(n))
    sps = []
    for s, p in temp:
        sps.append((s, int(p)))
    for i in answer(n, sps):
        print(i)


def __starting_point():
    main()

__starting_point()
