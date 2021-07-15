from itertools import chain
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        s = set(range(n))
        for c in chain(leftChild, rightChild):
            if c != -1:
                if c not in s:
                    return False
                s.remove(c)
                
        if len(s) != 1:
            return
        
        def dfs(node: int):
            if node == -1:
                return
            nonlocal n
            n -= 1
            dfs(leftChild[node])
            dfs(rightChild[node])
            
        dfs(s.pop())
        return n == 0
