class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        if not arr:
            return 0
        cum = 0
        odd, even = 0, 1
        res = 0
        MOD = 10**9 + 7
        for num in arr:
            cum += num
            if cum % 2:
                res += even
                odd += 1
            else:
                res += odd
                even += 1
            res %= MOD
        return res % MOD
