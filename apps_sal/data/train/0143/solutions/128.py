class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) <= 2:
            return len(tree)

        n = len(tree)
        res, l = 0, 0
        while l < n:
            type1, type2 = -1, -1
            next_l = -1
            for r in range(l, n):
                if type1 == -1:
                    type1 = tree[r]
                elif tree[r] != type1 and type2 == -1:
                    next_l = r
                    type2 = tree[r]
                elif tree[r] != type1 and tree[r] != type2:
                    break
                r += 1
            res = max(res, r - l)
            if r == n:
                break
            l = next_l
        return res
