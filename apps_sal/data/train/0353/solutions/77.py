class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, left, right = 0, 0, len(nums)-1        
        # Get rid of numbers that can never be included in the subsequences
        while right >= 0 and nums[right] + nums[left] > target:
            right -= 1
        
        while right >= 0:
            complement = target - nums[right]
            if nums[right] <= complement:
                if right >= left:
                    ans += (1 << (right + 1)) - 1
                else:
                    ans += (1 << (left)) - 1
                break
            else:
                while nums[left] <= complement:
                    left += 1
                
                if left == right:
                    ans += (1 << (left + 1)) - 2 # full empty & nums[right] itself
                    break
                else:
                    ans += ((1 << left) - 1) * (1 << (right - left))            
            right -= 1
            ans = ans % (10 ** 9 + 7)
            
        return ans % (10 ** 9 + 7)
    
    
# [5,5]
# 10

# [4,6]
# 10

