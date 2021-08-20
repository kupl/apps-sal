class Solution:

    def numOfSubarrays(self, A):
        MOD = 10 ** 9 + 7
        ans = 0
        even = odd = 0
        for x in A:
            if x % 2:
                (odd, even) = (1 + even, odd)
            else:
                even += 1
            ans = (ans + odd) % MOD
        return ans
