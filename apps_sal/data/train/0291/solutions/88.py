class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = int(1000000000.0 + 7)
        res = even = odd = 0
        for a in arr:
            even += 1
            if a % 2:
                (even, odd) = (odd, even)
            res = (res + odd) % MOD
        return res
