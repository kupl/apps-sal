class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        nTrees, ans = len(tree), 0
        if len(set(tree)) <= 2:
            return nTrees
        i, j = 0, 1
        while i < j and j < nTrees:
            if len(set(tree[i:j + 1])) <= 2:
                j += 1
                ans = max(ans, j - i)
            else:
                i += 1
        return ans
