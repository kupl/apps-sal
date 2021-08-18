class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        dp = [1 for i in range(n)]
        for i in range(n):
            start, end = 0, i - 1
            while(start <= end):
                if A[start] * A[end] < A[i]:
                    start += 1
                    continue
                if A[start] * A[end] > A[i]:
                    end -= 1
                    continue
                if start == end:
                    dp[i] += dp[start] * dp[end]
                else:
                    dp[i] += dp[start] * dp[end] * 2
                start += 1
                end -= 1
        return sum(dp) % (10**9 + 7)
