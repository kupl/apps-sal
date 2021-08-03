#!/usr/bin/env python3
from collections import deque
import sys
input = sys.stdin.readline


class DirectedGraph:
    def __init__(self, adj):
        self.n = len(adj)
        self.adj = adj
        self.is_asyclic = False
        self.max_path_len = None

    def topological_sort(self):
        indegree = [0] * self.n
        for vs in self.adj:
            for dest in vs:
                indegree[dest] += 1
        zero_v = []
        for v, indeg in enumerate(indegree):
            if indeg == 0:
                zero_v.append(v)
        max_path_len = 1
        tp_sorted = []
        to_be_added = []
        while True:
            while zero_v:
                v = zero_v.pop()
                tp_sorted.append(v)
                for dest in self.adj[v]:
                    indegree[dest] -= 1
                    if indegree[dest] == 0:
                        to_be_added.append(dest)
            if len(to_be_added) > 0:
                zero_v.extend(to_be_added)
                to_be_added = []
                max_path_len += 1
            else:
                break
        if len(tp_sorted) == self.n:
            self.is_asyclic = True
            self.max_path_len = max_path_len
            return tp_sorted
        else:
            self.is_asyclic = False
            return None


t = int(input())
for case in range(t):
    n, m = map(int, input().split())
    forward = [[] for _ in range(n)]
    backward = [[] for _ in range(n)]

    seen = set()
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if (u, v) in seen:
            continue
        seen.add((u, v))
        forward[u].append(v)
        backward[v].append(u)

    DG = DirectedGraph(forward)
    tps = DG.topological_sort()
    state = [-1] * n
    state[0] = 0
    for v in tps:
        if len(backward[v]) == 0:
            state[v] = 0
        for pv in backward[v]:
            state[v] = max(state[v], (state[pv] + 1) % 3)

    ans = []
    for i, color in enumerate(state):
        if color == 2:
            ans.append(i + 1)
    print(len(ans))
    print(*ans)
