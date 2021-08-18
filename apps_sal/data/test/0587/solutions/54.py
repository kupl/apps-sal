import heapq

from typing import List


def main():
    n, k = list(map(int, input().split()))
    v = []
    for _ in range(n):
        t, d = list(map(int, input().split()))
        v.append((t, d))

    print((vs(v, k)))


def vs(v: List[List[int]], k: int) -> int:
    v.sort(key=lambda x: x[1], reverse=True)

    h0 = []
    h1 = []
    s = set()
    types = 0
    op = 0

    for i in range(k):
        t, d = v[i]
        op += d

        if t in s:
            heapq.heappush(h0, d)
            continue

        types += 1
        s.add(t)

    for i in range(k, len(v)):
        t, d = v[i]

        if not t in s:
            s.add(t)
            heapq.heappush(h1, -d)

    result = op + types ** 2

    while len(h0) > 0 and len(h1) > 0:
        d0 = heapq.heappop(h0)
        d1 = -heapq.heappop(h1)
        op = op - d0 + d1
        types += 1
        tmp = op + types ** 2

        if tmp > result:
            result = tmp

    return result


def __starting_point():
    main()


__starting_point()
