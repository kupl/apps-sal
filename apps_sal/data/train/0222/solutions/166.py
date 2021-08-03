class Solution:
    def lenLongestFibSubseq(self, x: List[int]) -> int:
        def func(a, b):
            if (a, b) in dp:
                return dp[a, b]
            ans = 1
            if (a + b) in f:
                ans = 1 + func(b, a + b)
            dp[a, b] = ans
            return ans
        l = len(x)
        f = set(x)
        dp = {}
        ma = 2
        for i in range(l):
            a = x[i]
            for j in range(i + 1, l):
                b = x[j]
                ma = max(1 + func(a, b), ma)
        return ma if ma > 2 else 0
