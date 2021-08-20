from collections import defaultdict


class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        (l, r) = (0, 0)
        d = defaultdict(int)
        res = 0
        for r in range(len(tree)):
            d[tree[r]] += 1
            while len(d) > 2:
                d[tree[l]] -= 1
                if d[tree[l]] == 0:
                    d.pop(tree[l])
                l += 1
            res = max(res, r - l + 1)
        return res
