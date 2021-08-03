class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        parent = [-1] * 1000001

        def find(node):
            if parent[node] == -1:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(X, Y):
            parentX = find(X)
            parentY = find(Y)

            if parentX != parentY:
                parent[parentY] = parentX

        for node in A:
            for i in range(2, int(sqrt(node)) + 1):
                if node % i == 0:
                    union(i, node)
                    union(node, node // i)
        count = 0
        d = {}

        for node in A:
            parentNode = find(node)
            count = max(count, 1 + d.get(parentNode, 0))
            d[parentNode] = 1 + d.get(parentNode, 0)
        return count
