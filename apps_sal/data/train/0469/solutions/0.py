class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        leftset, rightset = set(leftChild), set(rightChild)
        roots = []
        for i in range(n):
            if i not in leftset and i not in rightset:
                roots.append(i)
                if len(roots) > 1:
                    return False
        if not roots:
            return False
        root = roots[0]

        nodes = []

        def dfs(root):
            if root == -1:
                return
            if len(nodes) > n:
                return
            nodes.append(root)
            dfs(leftChild[root])
            dfs(rightChild[root])
        dfs(root)
        return len(nodes) == n
