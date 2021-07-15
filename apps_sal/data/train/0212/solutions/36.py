class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        factors = set(A)
        A.sort()
        dp = defaultdict(int)
        count = 0
        modulus = 10**9 + 7
        for i in range(len(A)):
            dp[A[i]] += 1
            for j in range(i):
                if A[i] % A[j] == 0 and (A[i] // A[j]) in factors:
                    dp[A[i]] += dp[A[j]] * dp[A[i] // A[j]]
            count = (count + dp[A[i]]) % modulus
        return count
