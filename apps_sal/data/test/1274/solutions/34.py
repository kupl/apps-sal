import heapq

from typing import List


def main():
    n, k = list(map(int, input().split()))
    v = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        v.append((a, b))

    print((sv(v, k)))


def sv(v: List[List[int]], k: int) -> int:
    vv = {}
    for a, b in v:
        if str(a) in vv:
            vv[str(a)].append(b)
        else:
            vv[str(a)] = []
            vv[str(a)].append(b)

    hp = []
    result = 0
    bk = 1
    while k >= bk:
        if str(bk) in vv:
            for b in vv[str(bk)]:
                heapq.heappush(hp, -b)
        if len(hp) > 0:
            result += -heapq.heappop(hp)
        bk += 1

    return result


def __starting_point():
    main()


__starting_point()
