class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        output = 0
        
        count_odd = 0
        l = 0
        for r, n in enumerate(nums):
            
            count_odd += int(n % 2 == 1)
            
            n_even = 1
            for j in range(r+1, len(nums)):
                if nums[j] % 2 == 0:
                    n_even += 1
                else:
                    break
            
            while count_odd == k:
                output += n_even
                count_odd -= int(nums[l] % 2 == 1)
                l += 1
        
        return output
