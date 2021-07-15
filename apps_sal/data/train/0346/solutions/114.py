class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        left_left = 0
        left_right = 0
        odds_left = 0
        odds_right = 0
        
        odds = 0
        
        ret = 0
        
        for right in range(n):
            odds_left += nums[right] % 2
            odds_right += nums[right] % 2
            
            while left_left <= right and odds_left > k:
                odds_left -= nums[left_left] % 2
                left_left += 1
            
            while left_right <= right and odds_right - nums[left_right] % 2 >= k:
                odds_right -= nums[left_right] % 2
                left_right += 1
            
            if odds_left == odds_right == k:
                ret += (left_right - left_left + 1)
                
        
        
        return ret
