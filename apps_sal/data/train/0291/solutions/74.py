class Solution:

    def numOfSubarrays(self, A):
        MOD = 10 ** 9 + 7
        ans = 0
        tt = 0
        even = odd = 0
        for x in A:
            tt += x
            if tt % 2 == 0:
                ans = (ans + odd) % MOD
                even += 1
            else:
                ans = (ans + 1 + even) % MOD
                odd += 1
        return ans
