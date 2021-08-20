import sys
import copy
sys.setrecursionlimit(10 ** 9)


def dfs(seen, graph, i):
    for (v, w) in graph[i]:
        if seen[v - 1] != -1:
            continue
        seen[v - 1] = abs(w % 2 - seen[i])
        dfs(seen, graph, v - 1)


def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        (ui, vi, wi) = map(int, input().split())
        graph[ui - 1].append((vi, wi))
        graph[vi - 1].append((ui, wi))
    seen = [-1 for _ in range(n)]
    seen[0] = 0
    for i in range(n - 1):
        dfs(seen, graph, i)
    print(*seen, sep='\n')


main()
