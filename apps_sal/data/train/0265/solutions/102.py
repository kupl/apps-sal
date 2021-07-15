class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sums = [0 for num in nums]
        sum2index = {0:-1}
        nums_subarrays = [0 for num in nums]
        for i, num in enumerate(nums):
            if i == 0:
                sums[i] = nums[i]
            else:
                sums[i] = sums[i-1] + nums[i]
            if sums[i]-target in sum2index:
                if i == 0:
                    nums_subarrays[i] = 1
                else:
                    nums_subarrays[i] = max(nums_subarrays[i-1], nums_subarrays[sum2index[sums[i]-target]]+1)
            else:
                if i == 0:
                    nums_subarrays[i] = 0
                else:
                    nums_subarrays[i] = nums_subarrays[i-1]
            sum2index[sums[i]] = i
        return nums_subarrays[-1]
