from collections import Counter


class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        res = l = 0
        count = Counter()
        for (r, t) in enumerate(tree):
            count[t] += 1
            while len(count) >= 3:
                count[tree[l]] -= 1
                if count[tree[l]] == 0:
                    del count[tree[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
