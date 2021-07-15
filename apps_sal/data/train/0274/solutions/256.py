class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = collections.deque() # monotonically decreasing 
        mind = collections.deque() # monotonically increasing 
        i = 0
        # maxd[-1] gives last element and maxd[0] gives first/front element
        
        for num in nums:
            while maxd and num > maxd[-1]: maxd.pop() # biggr num eats up all smaller ones
            while mind and num < mind[-1]: mind.pop()
            maxd.append(num)
            mind.append(num)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i+=1
        return len(nums) -i
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # read - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609708/Python-Clean-Monotonic-Queue-solution-with-detail-explanation-O(N)

