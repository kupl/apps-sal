class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0 for i in range(n)]
        for i in range(len(leftChild)):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
                if indegree[leftChild[i]] > 1:
                    return False
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1
                if indegree[rightChild[i]] > 1:
                    return False
        root = -1
        for node in range(len(indegree)):
            if indegree[node] == 0:
                if root == -1:
                    root = node
                else:
                    return False
        if root == -1:
            return False

        def countNodes(root, l, r):
            if root is -1:
                return 0
            return 1 + countNodes(l[root], l, r) + countNodes(r[root], l, r)
        return countNodes(root, leftChild, rightChild) == n
