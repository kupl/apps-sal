from functools import reduce


class Solution:

    def validateBinaryTreeNodes(self, n, leftChild, rightChild) -> bool:
        g = dict(enumerate(zip(leftChild, rightChild)))
        root = set(range(n)) - reduce(set.union, list(map(set, [leftChild, rightChild])))
        if len(root) != 1:
            return False
        root = next(iter(root))

        def dfs(n):
            if n == -1:
                return True
            if n not in g:
                return False
            return all(map(dfs, g.pop(n)))
        out = dfs(root)
        return out and (not g)
