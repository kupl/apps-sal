class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        r = 0
        cur = 0
        n = len(nums)
        neg = -1
        zero = -1
        
        for i in range(n):
            if nums[i] < 0:
                cur += 1
                if neg == -1:
                    neg = i
            
            if nums[i] == 0:
                zero = i
                cur = 0
                neg = -1
            else:
                if cur % 2 == 0:
                    r = max(r, i - zero)
                else:
                    r = max(r, i - neg)
        return r
