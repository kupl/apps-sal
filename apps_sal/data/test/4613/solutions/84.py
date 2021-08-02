from collections import Counter, deque
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float("inf")

sys.setrecursionlimit(10**6)
def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    n, m = i_map()
    ab = [i_list() for i in range(m)]

    def dfs(table):
        visited = [1]
        que = [1]

        while que != []:
            now = que[0]
            del que[0]

            for index, e in enumerate(table[now]):
                if (e == 1) & (index not in visited):
                    visited.append(index)
                    que.append(index)
        if len(visited) == n:
            return 0
        else:
            return 1

    ans = 0
    for i in range(m):
        graph = ab.copy()
        del graph[i]
        table = [[0] * (n + 1) for i in range(n + 1)]
        for a, b in graph:
            table[a][b] = 1
            table[b][a] = 1

        ans += dfs(table)
    print(ans)


def __starting_point():
    main()


__starting_point()
