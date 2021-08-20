class Solution:

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], 0, 0, 1, k, n)
        return res

    def dfs(self, res, cur, d, s, b, k, n):
        if d == k and s == n:
            res.append(cur)
            return
        for i in range(b, 10):
            self.dfs(res, cur + [i], d + 1, s + i, i + 1, k, n)
