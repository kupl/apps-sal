class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        mod = 10**9 + 7
        A.sort()
        dp = [1 for _ in range(len(A))]
        reverse_map = {x: i for i, x in enumerate(A)}

        for i, x in enumerate(A):
            for j in range(i):
                if x % A[j] == 0:
                    right_child = x / A[j]
                    if right_child in reverse_map:
                        dp[i] += dp[j] * dp[reverse_map[right_child]]
                        dp[i] % mod

        return sum(dp) % mod
