import collections


class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        if n == 1:
            return True
        degree = [0] * n
        graph = []
        for _ in range(n):
            graph.append(set())
        for (i, v) in enumerate(leftChild):
            if v != -1:
                degree[v] += 1
                graph[i].add(v)
        for (i, v) in enumerate(rightChild):
            if v != -1:
                degree[v] += 1
                graph[i].add(v)
        root = [i for i in range(n) if degree[i] == 0]
        if len(root) != 1:
            return False
        visited = set()
        self.dfs(root[0], graph, visited)
        if len(visited) != n:
            return False
        counter = collections.Counter(degree)
        return len(counter) == 2 and counter[0] == 1 and (counter[1] == n - 1)

    def dfs(self, idx, graph, visited):
        visited.add(idx)
        for j in graph[idx]:
            if j not in visited:
                self.dfs(j, graph, visited)
