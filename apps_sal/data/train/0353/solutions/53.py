# binary search, O(nlogn)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        
        def bsearch(t, l, r):
            if l > r: return -1
            while l < r:
                m = (l + r + 1) // 2
                if nums[m] <= t:
                    l = m
                else:
                    r = m - 1
            return l if nums[l] <= t else -1
        
        res = 0
        for i, n in enumerate(nums):
            ind = bsearch(target - n, 0, i - 1)
            must_have = pow(2, ind + 1, MOD) - 1
            may_have = pow(2, max(0, i - ind - 1), MOD)
            res = (res + must_have * may_have) % MOD
            
        # add special case of single element subsequence
        res = (res + sum(2 * n <= target for n in nums)) % MOD
        return res
        # AC: 2320 ms, beats 41.74%, 25.2 MB, beats 81.62%
            

