class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = list(range(n))
        degree = [0] * n
        count = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count, parent
            xp, yp = find(x), find(y)
            if xp != yp:
                count -= 1
                parent[yp] = xp

        for par, nodes in enumerate(zip(leftChild, rightChild)):
            l, r = nodes
            if l != -1:
                degree[l] += 1
                union(par, l)
            if r != -1:
                degree[r] += 1
                union(par, r)

        return True if sum(degree) == n - 1 and count == 1 else False
