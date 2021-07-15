from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx, mn = deque([0]),deque([0])
        result = 1
        l = 0
        
        for i in range(1,len(nums)):
            while len(mx) != 0 and nums[mx[-1]] < nums[i]:
                mx.pop()
            mx.append(i)
            while len(mn) != 0 and nums[mn[-1]] > nums[i]:
                mn.pop()
            mn.append(i)
            
            while mx and mn and nums[mx[0]] -nums[mn[0]] > limit:
                l +=1
                while mx[0] < l:
                    mx.popleft()
                while mn[0] < l:
                    mn.popleft()
                
            result = max(result, i-l+1)
        return result

