class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        (i, j) = (0, 0)
        res = 0
        d = {}
        while j < len(tree):
            d[tree[j]] = d.get(tree[j], 0) + 1
            if len(d) <= 2:
                res = max(res, j - i + 1)
            else:
                while len(d) > 2:
                    d[tree[i]] = d[tree[i]] - 1
                    if d[tree[i]] == 0:
                        d.pop(tree[i])
                    i += 1
            j += 1
        return res
