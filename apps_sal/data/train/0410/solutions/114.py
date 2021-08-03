class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = {}

        def helper(i):
            if i == 1:
                return 0
            if i in d:
                return d[i]
            if i % 2 == 0:
                return 1 + helper(i // 2)
            else:
                return 1 + helper(3 * i + 1)
        ans = [[helper(i), i] for i in range(lo, hi + 1)]
        ans.sort()
        return ans[k - 1][1]
