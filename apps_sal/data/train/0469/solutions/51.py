class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        allChildren = [n for n in leftChild + rightChild if n != -1]
        allChildrenSet = set(allChildren)
        if not(len(allChildren) == len(allChildrenSet)):
            return False
        
        root = [i for i in range(n) if i not in allChildrenSet]
        if len(root) != 1:
            return False
        
        root = root[0]
        stk = [root]
        while stk:
            n = stk.pop()
            allChildrenSet.discard(n)
            stk.extend([c for c in [leftChild[n], rightChild[n]] if c != -1])
        
        return not allChildrenSet
