class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        memo = {0: 0, 1: 0}
        cumsum = 0

        res = 0

        for v in arr:
            cumsum += v

            if cumsum % 2 == 0:
                memo[0] += 1
                res = (res + memo[1]) % MOD

            else:
                memo[1] += 1
                res = (1 + res + memo[0]) % MOD

        return res
