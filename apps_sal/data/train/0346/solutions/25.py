class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''
        This is not an atmost/atleast constraint. 
        Soln pattern is different for atleast constraint
        refer this https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
        This is an exact constraint, so different thinking is required
        
        Nice solution is explained here
        https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-O(1)-Space
        Two methods are given.
        1) uses standard templete to find subarray with atmost k odd numbers
        2) modifies this template slightly to accomodate exactly k odd numbers constraint
        '''
        # return self.sol2(nums, k)
        return self.sol1(nums, k) - self.sol1(nums, k-1)
    
    def sol1(self, nums, k):
        '''
        Exactly k ones = atMost(k ones) - atMost(k-1 ones)
        '''
        start = 0
        odds = 0
        res = 0
        for end in range(len(nums)):
            odds += nums[end] & 1
            while odds > k:
                '''Inc start till constraint is violated'''
                odds -= nums[start] & 1
                start += 1
            
            '''
            This will add all sub arrays from size 1,2..end-start for every iteration
            Since we are doing atMost(k) even if sub array does not contain any odd number we still have to add it to res even if its size is 1
            '''
            res += end - start + 1
            # print(res)    
        return res
    
    def sol2(self, nums, k):
        start = 0
        odds = 0
        res = 0
        count = 0
        for end in range(len(nums)):
            if nums[end] & 1: # nums[end] is odd
                odds += 1
                count = 0 # reset counter to avoid repeated addition to result
                
            while odds >= k:
                if nums[start] & 1:
                    odds -= 1
                    
                start += 1
                count += 1
                # print(end, start)
                
                
            res += count
                
        return res

