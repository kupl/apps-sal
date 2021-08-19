class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        k = 2
        n = len(tree)
        if n < k:
            return n
        i = 0
        lookup = {}
        ans = 0
        for j in range(n):
            lookup[tree[j]] = j
            if len(lookup) > k:
                i_min = min(lookup.values())
                del lookup[tree[i_min]]
                i = i_min + 1
            ans = max(ans, j - i + 1)
        return ans
