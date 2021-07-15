class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        
        # It is OK to sort the array because the question
        # is essentially asking for the number of subsets,
        # and the order doesn't matter.
        nums.sort()
        i, j = 0, len(nums)-1
        count = 0
        
        # nums[i] is the minimum element,
        # nums[j] is the maximum element,
        # a subset starting with the minimum element
        # contains at least the minimum element.
        # for nums[i+1] to nums[j], it can be included or not.
        # So totally there are 2 ** (j-i) subsets.
        while i <= j:
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i <= j:
                # Compare to (2 ** (j-1)) % mod,
                # using pow function is faster.
                count += pow(2, j-i, mod)
                i += 1
        return count % mod
