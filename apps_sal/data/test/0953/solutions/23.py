"""http://codeforces.com/problemset/problem/500/B"""
from collections import defaultdict


class DFS:
    visited = None
    graph = None

    def __init__(self, graph):
        self.visited = set()
        self.graph = graph

    def dfs(self, node):
        self.visited.add(node)
        for v in self.graph[node]:
            if v not in self.visited:
                self.dfs(v)


def solve(n, p, m):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if m[i][j] == '1':
                graph[i].append(j)
    for num in range(1, n + 1):
        i = p.index(num)
        d = DFS(graph)
        d.dfs(i)
        for j in range(i):
            if j in d.visited and p[i] < p[j]:
                (p[i], p[j]) = (p[j], p[i])
    return ' '.join(map(str, p))


def __starting_point():
    n = int(input())
    p = list(map(int, input().split()))
    matrix = [input() for _ in range(n)]
    print(solve(n, p, matrix))


__starting_point()
