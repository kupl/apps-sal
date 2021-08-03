class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A = sorted(A)
        mems = {}
        for ix in range(len(A)):
            mems[A[ix]] = ix

        dp = [1] * len(A)

        big_mod = 10**9 + 7

        for i in range(len(A)):
            extras = 0
            for j in range(i):
                d, mo = divmod(A[i], A[j])
                if mo == 0:
                    if d in mems:
                        extras += dp[j] * dp[mems[d]]
                        extras = extras % big_mod

            dp[i] += extras

        result = sum(dp) % big_mod

        return result
