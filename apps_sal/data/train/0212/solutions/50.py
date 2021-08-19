class Solution:

    def numFactoredBinaryTrees(self, x: List[int]) -> int:

        def f(n):
            if n in dp:
                return dp[n]
            ans = 1
            for i in x:
                if i > n ** 0.5:
                    break
                if n % i == 0 and n // i in se:
                    ans += (1 if n // i == i else 2) * f(i) * f(n // i)
            dp[n] = ans
            return ans
        dp = {}
        x.sort()
        se = set(x)
        ans = 0
        for i in x:
            ans += f(i)
        return ans % (10 ** 9 + 7)
