class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        winMax = [0]
        winMin = [0]

        i = j = 0
        res = 0
        while i<len(nums)-1 and j<len(nums)-1:
            
            diff = nums[winMax[0]] - nums[winMin[0]]
            #print(i,j,diff,winMax,winMin)
            if diff <= limit:
                res = max(res,j-i+1)
                
            if diff <= limit:
                j += 1
                while winMax and nums[j]>nums[winMax[-1]]:
                    winMax.pop(-1)
                winMax.append(j)
                while winMin and nums[j]<nums[winMin[-1]]:
                    winMin.pop(-1)
                winMin.append(j)

            else:
                if i == winMax[0]:
                    winMax.pop(0)
                if i == winMin[0]:
                    winMin.pop(0)
                i += 1
                
        diff = nums[winMax[0]] - nums[winMin[0]]
        if diff <= limit:
            res = max(res,j-i+1)
            
        return res
                

