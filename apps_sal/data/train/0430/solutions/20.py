class Solution:
    def distinctSubseqII(self, S: str) -> int:
        # Dynamic Programming
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # dp, last = [1], {}
        # for i, x in enumerate(S):
        #     dp.append(dp[-1] * 2)
        #     if x in last:
        #         dp[-1] -= dp[last[x]]
        #     last[x] = i

        # return (dp[-1] - 1) % (10**9 + 7)


        dp, MOD = [0] * len(S), 10**9 + 7
        for i, char in enumerate(S):
            ind = S.rfind(char, 0, i)
            dp[i] = 1 + sum(dp[:i]) % MOD if ind == -1 else sum(dp[ind:i]) % MOD
        return sum(dp) % MOD

