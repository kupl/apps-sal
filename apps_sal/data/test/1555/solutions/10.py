import collections
import heapq
import bisect
import math
import time


class Solution2:
    def solve(self, A1, A2):
        pass


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return b * a // gcd(b, a)


class Solution:

    def solve(self, grid):
        def union(i, j):
            leader_i, leader_j = find(i), find(j)
            sets[leader_j] = sets[i] = sets[j] = leader_i

        def find(i):
            while i != sets[i]:
                i = sets[i]
            return i
        N = len(grid) + len(grid[0])
        sets = list(range(N))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '=':
                    union(i, j + len(grid))

        graph = collections.defaultdict(set)
        inc = collections.defaultdict(set)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                leader_i, leader_j = find(i), find(j + len(grid))
                if grid[i][j] == '>':
                    if leader_i == leader_j:
                        print("No")
                        return
                    graph[leader_j].add(leader_i)
                    inc[leader_i].add(leader_j)
                elif grid[i][j] == '<':
                    if leader_i == leader_j:
                        print("No")
                        return
                    graph[leader_i].add(leader_j)
                    inc[leader_j].add(leader_i)

        self.levels = [0] * N

        def dfs(node, level):
            self.levels[node] = max(self.levels[node], level)
            if not inc[node]:
                seen.add(node)
                for next_node in graph[node]:
                    inc[next_node].discard(node)
                    dfs(next_node, self.levels[node] + 1)

        seen = set()
        for i in range(N):
            l = find(i)
            if not inc[l] and l not in seen:
                seen.add(l)
                dfs(l, 1)

        if any(inc[find(node)] for node in range(N)):
            print("No")
            return

        for i in range(N):
            l = find(i)
            if l != i:
                self.levels[i] = self.levels[l]

        print("Yes")
        print(' '.join(str(o) for o in self.levels[:len(grid)]))
        print(' '.join(str(o) for o in self.levels[len(grid):]))


sol = Solution()
sol2 = Solution2()

for test_case in range(1):
    N, M = input().split()
    a = []
    for _ in range(int(N)):
        a.append(input())

    out = sol.solve(a)
