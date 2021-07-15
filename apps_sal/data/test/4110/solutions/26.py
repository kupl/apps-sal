import copy
import heapq

from typing import List, Tuple


def main():
    d, g = list(map(int, input().split()))
    v = []
    for _ in range(d):
        p, c = list(map(int, input().split()))
        v.append((p, c))

    print((ag(v, g)))


def ag(v: List[Tuple[int, int]], g: int) -> int:
    rs = []
    # ex. [(3, 500), (5, 800)] -> [(1, 3, 500), (2, 5, 800)]
    v = [(i, p, c) for i, (p, c) in enumerate(v, 1)]

    for j in range(2 ** len(v)):
        cb = []
        for k in range(len(v)):
            if ((j >> k) & 1):
                cb.append(v[k])

        sc = 0
        cnt = 0
        # calc bonus score
        for (i, p, c) in cb:
            sc += i * 100 * p + c
            cnt += p

        vv = [x for x in copy.copy(v) if not x in cb]
        while sc < g:
            if not vv:
                break
            i, p, _ = vv.pop()
            for _ in range(p - 1):
                if sc >= g:
                    break
                sc += i * 100
                cnt += 1

        if sc >= g:
            heapq.heappush(rs, cnt)
    return heapq.heappop(rs)


def __starting_point():
    main()

__starting_point()
