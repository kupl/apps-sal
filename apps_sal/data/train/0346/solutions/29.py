class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Sliding window approach
        num_odd_numbers = 0
        foo = 0
        left = 0
        right = 0
        
        # We keep an extra count variable here: after we break out of the inner while loop, 
        # we will have the number of nice subarrays recorded as count, then we will continue to expand the right 
        # part of the window, as long as it doesn't hit another odd number which will make the window 
        # unsatisfactory (this is where we reset the count to 0), there will be the same amount more of the 
        # satisfactory window (imagine when K = 2, if [1, 1, 2, 2] is satistfactory, [1, 1, 2, 2, 2] is statisfactory too).
        count = 0
        num_nice_arrays = 0
        
        while right < len(nums):
            r_n = nums[right]
            if r_n % 2 == 1:
                count = 0
                num_odd_numbers += 1
                
            while num_odd_numbers == k:
                # Try to subtract the window
                l_n = nums[left]
                if l_n % 2 == 1:
                    num_odd_numbers -= 1
                left += 1
                count += 1
              
            num_nice_arrays += count
            right += 1
            
        return num_nice_arrays
