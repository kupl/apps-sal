class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        root = set(range(n))
        for c in leftChild + rightChild:
            if c == -1:
                continue
            if c not in root:
                return False
            root.remove(c)
        
        if len(root) != 1:
            return False
        
        def dfs(node):
            if node == -1:
                return 0
            
            return 1 + dfs(leftChild[node]) + dfs(rightChild[node])
        
        return dfs(root.pop()) == n
