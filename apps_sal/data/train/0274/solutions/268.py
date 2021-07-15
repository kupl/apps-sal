from collections import deque
class Solution:
    def longestSubarray(self, nums, limit):
        mini, maxi, res, j  = deque([]), deque([]), 0, 0

        for i in range(len(nums)):
            while mini and mini[-1][0] > nums[i]:
                mini.pop()
            mini.append([nums[i], i])
            
            while maxi and maxi[-1][0] < nums[i]:
                maxi.pop()
            maxi.append([nums[i], i])
                
            while(maxi[0][0] -  mini[0][0] > limit) and j < i :
                if mini[0][1] <= j:
                    mini.popleft()
                    
                elif maxi[0][1] <= j:
                    maxi.popleft()
                    
                j +=1
            res = max(res, i-j+1)
            
        return res
