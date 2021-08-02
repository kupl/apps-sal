class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        dp = triangle.pop()

        while triangle:
            level = triangle.pop()

            for i in range(len(level)):
                dp[i] = min(dp[i], dp[i + 1]) + level[i]

        return dp[0]
