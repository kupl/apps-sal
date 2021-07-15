class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = r = 0
        minq = collections.deque()
        maxq = collections.deque()
        ans = 0
        
        while r < len(nums):
            while minq and nums[minq[-1]] >= nums[r]:
                minq.pop()
            while maxq and nums[maxq[-1]] <= nums[r]:
                maxq.pop()
                
            minq.append(r)
            maxq.append(r)
            
            while nums[maxq[0]] - nums[minq[0]] > limit:
                l += 1
                if l > minq[0]:
                    minq.popleft()
                if l > maxq[0]:
                    maxq.popleft()
                    
            ans = max(ans, r - l + 1)
            r += 1
            
        return ans

