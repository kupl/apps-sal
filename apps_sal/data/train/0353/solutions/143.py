class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        result = 0
        for i in range(len(nums)):
            if nums[i] <= target // 2:
                left, right = i, len(nums) - 1
                while left < right - 1:
                    mid = (left + right) //  2
                    if nums[mid] <= target - nums[i]:
                        left = mid
                    else:
                        right = mid - 1
                if nums[i] + nums[right] <= target:
                    result += 2**(right - i)
                elif nums[i] + nums[left] <= target:
                    result += 2**(left - i)
        return result % MOD
                    
                    

