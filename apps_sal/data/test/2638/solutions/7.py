class Solution:
    def nodeSum(self, L, U):
        ans = [0] * len(U)
        for i, v in enumerate(U):
            ans[i] = (v + min(L[i], L[i + 1]))
        return ans

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        L = triangle[-1]
        for i in range(len(triangle) - 1, 0, -1):
            L = self.nodeSum(L, triangle[i - 1])
        return L[0]
