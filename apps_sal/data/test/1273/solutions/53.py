# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, ABs):
    tree_top = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        tree_top[ABs[i][0]].append(i)
        tree_top[ABs[i][1]].append(i)

    max_color = 0
    for tt in tree_top:
        max_color = max(max_color, len(tt))

    ans = [0 for _ in range(N - 1)]
    for tt in tree_top:
        colored = []
        for i in tt:
            if ans[i] != 0:
                colored.append(ans[i])
        colored.sort()
        now_color = 1
        colored_point = 0
        for i in tt:
            if ans[i] != 0:
                continue
            if colored_point < len(colored) \
                    and now_color == colored[colored_point]:
                now_color += 1
                colored_point += 1
            ans[i] = now_color
            now_color += 1

    print(max_color)
    for a in ans:
        print(a)


def __starting_point():
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    ABs = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, ABs)

__starting_point()
