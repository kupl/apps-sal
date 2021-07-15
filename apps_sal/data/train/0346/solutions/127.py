class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:        
        def at_most(k):
            start_ptr = 0
            result = 0
            
            for end_ptr in range(len(nums)):
                k -= nums[end_ptr] % 2
                
                while k < 0: # Already satisfied the condition, let's reduce the window size
                    k += nums[start_ptr] % 2
                    start_ptr += 1
                
                result += end_ptr - start_ptr + 1   # Now k just hit > 0, so we can compute this. No of subarray possible is end_ptr - start_ptr + 1. Start_ptr would have gotten as close as possible after this. 
            
            return result
            
        return at_most(k) - at_most(k - 1)

