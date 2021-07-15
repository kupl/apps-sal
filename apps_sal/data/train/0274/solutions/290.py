class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = deque()
        minq = deque()
        k = 0
        for i in nums:
            while maxq and i > maxq[-1]: maxq.pop()
            while minq and i < minq[-1]: minq.pop()  
            maxq.append(i)
            minq.append(i)
            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[k]: maxq.popleft()
                if minq[0] == nums[k]: minq.popleft()
                k += 1
        return len(nums)-k
            
            

