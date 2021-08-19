class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        res = even = odd = 0
        for x in arr:
            even += 1
            if x % 2 != 0:
                (odd, even) = (even, odd)
            res = (res + odd) % (10 ** 9 + 7)
        return res
