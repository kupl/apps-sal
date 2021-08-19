def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    (h, w) = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(map(int, input().split())) for _ in range(h)]
    c = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            c[i][j] = abs(a[i][j] - b[i][j])
    mid = 6400
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1 << mid + c[0][0] | 1 << mid - c[0][0]
    for x in range(h):
        for y in range(w):
            for (dx, dy) in [[0, 1], [1, 0]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < h and 0 <= ny < w:
                    dp[nx][ny] = dp[nx][ny] | dp[x][y] << c[nx][ny]
                    dp[nx][ny] = dp[nx][ny] | dp[x][y] >> c[nx][ny]
    for i in range(mid + 1):
        if dp[-1][-1] >> i & 1:
            res = mid - i
    print(res)


def __starting_point():
    main()


__starting_point()
