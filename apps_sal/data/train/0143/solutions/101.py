from collections import OrderedDict


class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        last_index_of = OrderedDict()
        ans = l = 0
        for (i, t) in enumerate(tree):
            last_index_of[t] = i
            last_index_of.move_to_end(t)
            if len(last_index_of) > 2:
                ans = max(ans, i - l)
                l = last_index_of.popitem(last=False)[1] + 1
        ans = max(ans, len(tree) - l)
        return ans
