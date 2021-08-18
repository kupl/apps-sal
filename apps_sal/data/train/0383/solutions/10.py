class UF:
    def __init__(self, n):
        self.arr = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def root(self, x):
        curr = x

        while curr != self.arr[curr]:
            curr = self.arr[curr]
        return curr

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)

        rank_x = self.rank[root_x]
        rank_y = self.rank[root_y]

        if rank_x >= rank_y:
            self.arr[root_y] = root_x
            self.rank[root_x] += rank_y
        else:
            self.arr[root_x] = root_y
            self.rank[root_y] += rank_x


class Solution:

    def dfs(self, root, seen, uf, intersection):

        for i, v in enumerate(self.graph[root]):
            if v == 0:
                continue

            if i in self.init_set:
                if root not in intersection:
                    intersection[root] = []
                intersection[root].append(i)
                continue

            uf.union(root, i)
            if i in seen:
                continue
            seen.add(i)
            self.dfs(i, seen, uf, intersection)

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        self.graph = graph
        self.init_set = set(initial)
        initial.sort()

        uf = UF(len(graph[0]))
        seen = set()
        intersection = {}
        for node in range(len(graph[0])):
            if node in self.init_set:
                continue

            self.dfs(node, seen, uf, intersection)

        islands = {}
        for node in range(len(graph[0])):
            root = uf.root(node)
            if root not in islands:
                islands[root] = set()

            if node in intersection:
                for elt in intersection[node]:
                    islands[root].add(elt)
        islandCounts = {}
        for node in range(len(graph[0])):
            root = uf.root(node)
            if len(islands[root]) == 1:
                for key in islands[root]:
                    if key not in islandCounts:
                        islandCounts[key] = 1
                    else:
                        islandCounts[key] += 1
        if len(islandCounts) == 0:
            return initial[0]
        res = sorted(islandCounts, key=lambda x: (-islandCounts[x], x))
        return res[0]
