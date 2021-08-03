class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        if not arr:
            return 0

        n_even = 0
        n_odd = 0
        res = 0

        for x in arr:

            if x % 2 == 0:
                n_even, n_odd = n_even + 1, n_odd
            else:
                n_even, n_odd = n_odd, n_even + 1

            res += n_odd

        return res % (10**9 + 7)
