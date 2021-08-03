class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        parent = {x: 0 for x in range(n)}
        child = [0] * n
        val = {0: 0, 1: 0}
        for i in range(n):
            if leftChild[i] != -1:
                parent[leftChild[i]] += 1
                child[i] += 1
                if parent[leftChild[i]] > 1:
                    return False

            if rightChild[i] != -1:
                parent[rightChild[i]] += 1
                child[i] += 1
                if parent[rightChild[i]] > 1:
                    return False

        self.ans = 1

        def dfs(node):
            if leftChild[node] != -1:
                self.ans += 1
                dfs(leftChild[node])
            if rightChild[node] != -1:
                self.ans += 1
                dfs(rightChild[node])
        for i in range(n):
            val[parent[i]] += 1
            if parent[i] == 0:
                dfs(i)

        if self.ans == n:
            return True

        return False
