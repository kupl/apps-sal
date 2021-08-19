class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        for i in leftChild:
            if i >= 0:
                indegree[i] += 1
        for i in rightChild:
            if i >= 0:
                indegree[i] += 1
        root = -1
        for (i, d) in enumerate(indegree):
            if d == 0:
                root = i
                break
        if root < 0:
            return False
        visited = [False] * n
        res = True

        def dfs(node):
            if visited[node]:
                nonlocal res
                res = False
                return
            visited[node] = True
            if leftChild[node] >= 0:
                dfs(leftChild[node])
            if rightChild[node] >= 0:
                dfs(rightChild[node])
        dfs(root)
        for node in range(n):
            if not visited[node]:
                res = False
        return res
