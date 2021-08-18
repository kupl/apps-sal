class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        vis = set()
        heads = set()

        def dfs(i):
            if i == -1:
                return True
            vis.add(i)
            for child in [leftChild[i], rightChild[i]]:
                if child in vis:
                    if child not in heads:
                        return False
                    else:
                        heads.remove(child)
                else:
                    if not dfs(child):
                        return False
            return True

        for i in range(n):
            if i not in vis:
                if not dfs(i):
                    return False
                heads.add(i)

        return len(heads) == 1
