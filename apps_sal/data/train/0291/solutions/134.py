class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        cumsum = 0
        even = 1
        odd = 0
        ans = 0
        MOD = 10 ** 9 + 7
        for num in arr:
            cumsum += num
            if cumsum % 2 == 0:
                ans = (ans + odd) % MOD
                even += 1
            else:
                ans = (ans + even) % MOD
                odd += 1
        return ans
