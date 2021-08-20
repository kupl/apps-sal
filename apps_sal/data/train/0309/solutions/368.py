class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [[1 for i in range(1001)] for j in range(len(A))]
        lastIndex = {}
        ans = 1
        for (i, num) in enumerate(A):
            for j in range(1001):
                commonDiff = j - 500
                lastNumIndex = lastIndex.get(num - commonDiff, -1)
                if lastNumIndex >= 0 and lastNumIndex < i:
                    dp[i][j] = dp[lastNumIndex][j] + 1
                    ans = max(ans, dp[i][j])
            if num not in lastIndex:
                lastIndex[num] = -1
            lastIndex[num] = i
        return ans
