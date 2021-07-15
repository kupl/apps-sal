from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = deque()
        maxq = deque()
        ret=l=0
        for i in range(len(nums)):
            n = nums[i]
            while minq and n<minq[-1]:
                minq.pop()
            minq.append(n)
            while maxq and n>maxq[-1]:
                maxq.pop()
            maxq.append(n)
            while maxq[0]-minq[0]>limit:
                if minq[0]==nums[l]:
                    minq.popleft()
                if maxq[0]==nums[l]:
                    maxq.popleft()
                l+=1
            ret = max(ret,i-l+1)
        return ret
