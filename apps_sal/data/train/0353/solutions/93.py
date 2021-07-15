class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i,j, count = 0, len(nums) - 1, 0
        
        while i <= j:    
            if nums[i] + nums[j] <= target:
                count += int(pow(2, j - i - 1) * 2)
                i += 1
            else:
                j -= 1
                
        
        return count % (pow(10, 9) + 7)
