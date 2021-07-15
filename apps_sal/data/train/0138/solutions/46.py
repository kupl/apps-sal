class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        neg = 0
        lo, hi = 0, -1
        for i, num in enumerate(nums):
            if num == 0:
                lo = i+1
                neg = 0
            elif num < 0:
                neg += 1
            hi = i
            if neg % 2 == 0:
                #print(lo,hi)
                ans = max(ans, hi - lo + 1)
                
        neg = 0
        nums = nums[::-1]
        lo, hi = 0, -1
        for i, num in enumerate(nums):
            if num == 0:
                lo = i+1
                neg = 0
            elif num < 0:
                neg += 1
            hi = i
            if neg % 2 == 0:
                #print(lo,hi)
                ans = max(ans, hi - lo + 1)        

        return ans         

