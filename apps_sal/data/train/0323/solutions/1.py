class Solution:

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        (l1, l2, l3) = (len(s1) + 1, len(s2) + 1, len(s3) + 1)
        dp = [True for i in range(l2)]
        for i in range(1, l2):
            dp[i] = dp[i - 1] and s2[i - 1] == s3[i - 1]
        for i in range(1, l1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, l2):
                dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1] or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1]
