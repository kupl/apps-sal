import itertools
from typing import List, Tuple


def main():
    (d, g) = list(map(int, input().split()))
    v = []
    for _ in range(d):
        (p, c) = list(map(int, input().split()))
        v.append((p, c))
    print(ag(v, g))


def ag(v: List[Tuple[int, int]], g: int) -> int:
    ret = 10 ** 10
    for comb in itertools.product((False, True), repeat=len(v)):
        (cnt, score) = (0, 0)
        for (i, bit) in enumerate(comb):
            if bit:
                score += (i + 1) * 100 * v[i][0] + v[i][1]
                cnt += v[i][0]
        if score < g:
            idx = len(v) - list(reversed(comb)).index(False) - 1
            add = (g - score + (idx + 1) * 100 - 1) // ((idx + 1) * 100)
            if add < v[idx][0]:
                cnt += add
            else:
                cnt = 10 ** 10
        ret = min(ret, cnt)
    return ret


def __starting_point():
    main()


__starting_point()
