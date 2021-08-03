class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        n = len(A)
        A.sort()
        dp = [1] * n
        res = 0
        for i in range(n):
            s = 0
            e = i - 1
            for s in range(i):
                while s <= e and A[s] * A[e] > A[i]:
                    e -= 1

                if s > e:
                    break

                if A[s] * A[e] == A[i]:
                    dp[i] += ((dp[s] * dp[e] * 2) if s != e else (dp[s] * dp[e]))
                    dp[i] = dp[i] % (10 ** 9 + 7)
                    e -= 1

            res += dp[i]
            res = res % (10 ** 9 + 7)

        return res
