class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[float('inf') for _ in range(k)] for _ in range(n)]

        def getMinChange(i, j):
            count = 0
            while i < j:
                if s[i] != s[j]:
                    count += 1
                i += 1
                j -= 1
            return count
        dic = collections.defaultdict(int)
        for i in range(n):
            for j in range(i, n):
                dic[i, j] = getMinChange(i, j)
        for i in range(n):
            for j in range(k):
                if j >= i:
                    dp[i][j] = 0
                if j == 0:
                    dp[i][j] = dic[0, i]
        z = k
        for i in range(n):
            for k in range(1, z):
                for j in range(0, i):
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + dic[j + 1, i])
        return dp[n - 1][z - 1]
