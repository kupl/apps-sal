class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = []
        count = 0
        for i, val in enumerate(nums):
            if val == 0:
                if count > 0:
                    res.append(count)
                    count = 0
                res.append(0)
            elif val == 1:
                count += 1
        if count > 0:
            res.append(count)
        lenRes = len(res)
        ma = 0
        if lenRes > 2:
            for i in range(1, lenRes-1):
                ma = max(max(ma, res[i-1] + res[i+1]), max(res[i-1], res[i]), max(res[i+1], res[i]))
            return ma
        
        else:
            if lenRes == 1 and res[0] > 0:
                return res[0] - 1
            elif lenRes == 1 and res[0] == 0:
                return ma
            elif lenRes == 2:
                return max(res[0], res[1])
            
                
            
        
        
        
        
            

