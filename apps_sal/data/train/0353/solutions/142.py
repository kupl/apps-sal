class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # sort first
        nums.sort()

        # sliding windows
        n = len(nums)
        res = 0

        # one length subsequence
        mod = 10**9 + 7
        i, j = 0, n - 1

        # -> <-

        # i: min start, move ->
        for i in range(n):
            # j: max, move <- until we find the boundary
            while j >= i and nums[i] + nums[j] > target:
                j -= 1
            # anything in between [i,j] is answer. You always have i as _min + subsets of (j-i) would be answer. # combo = 2^(j-i)
            if i <= j and nums[i] + nums[j] <= target:
                res += pow(2, (j - i), mod)
                res %= mod

        return res
