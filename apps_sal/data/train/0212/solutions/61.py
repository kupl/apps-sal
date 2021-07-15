class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        dp = defaultdict(int)
        res = 0
        for i, num in enumerate(A):
            dp[num] = 1
            for j in range(i):
                if num % A[j] == 0:
                    dp[num] += dp[A[j]] * dp[A[i]//A[j]]
            res += dp[num]
        return res % 1000000007

