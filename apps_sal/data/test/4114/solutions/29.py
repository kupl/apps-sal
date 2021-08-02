#!/usr/bin/env python3


def solve(n, queries):
    def calcTopHeight(h, x, y, cx, cy):
        return h + abs(x - cx) + abs(y - cy)

    def calcHeight(h, x, y, cx, cy):
        return max(h - abs(x - cx) - abs(y - cy), 0)
    cand = [query for query in queries if query[2] != 0][0]
    for cx in range(101):
        for cy in range(101):
            cnt = 0
            probHeight = calcTopHeight(cand[2], cand[0], cand[1], cx, cy)
            for query in queries:
                x, y, h = query
                if calcHeight(probHeight, x, y, cx, cy) == h:
                    cnt += 1
            if cnt == n:
                return cx, cy, probHeight
    return -1, -1, -1


def main():
    N = int(int(input()))
    queries = [list(map(int, input().split())) for _ in range(N)]
    print((*solve(N, queries)))
    return
    # write c


def __starting_point():
    main()


__starting_point()
