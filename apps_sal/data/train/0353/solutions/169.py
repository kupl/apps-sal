class Solution:
    def numSubseq(self, nums, target: int) -> int:

        n = len(nums)
        nums.sort()
        res = 0
        i = 0
        last = n-1
        while i<n and 2*nums[i]<=target:
            j = last
            while j>=i and nums[i]+nums[j]>target:
                j -= 1
            last = j
            if i == j:
                res += 1
            else:
                res += 2**(j-i)   %1000000007
            i += 1
        return res%1000000007
