class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        dp = {n: 1 for n in A}
        setA = set(A)
        for i in range(len(A)): # goal
            target = A[i]
            for j in range(0, i): # using this as factor
                factor = A[j]
                if target%factor == 0:
                    other_half = target//factor
                    if other_half in setA:
                        dp[target] += dp[other_half] * dp[factor]
        return sum(dp.values())%(10**9 + 7)
