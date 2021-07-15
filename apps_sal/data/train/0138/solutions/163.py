class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def check(arr) -> int:
            if not arr:
                return 0
            pos = neg = -1
            pre_prod = 1
            res = 0
            for i,a in enumerate(arr):
                pre_prod *= a
                if pre_prod > 0:
                    if pos == -1:
                        pos = i
                    res = i+1
                else:
                    if neg == -1:
                        neg = i
                    res = max(res, i-neg)
            return res
        
        res = i = j = 0
        while j < len(nums):
            while j < len(nums) and nums[j] == 0:
                j += 1
            i = j
            while j < len(nums) and nums[j] != 0:
                j += 1
            # print(str(i)+'->'+str(j))
            if j-i > res:
                res = max(res, check(nums[i:j]))
        return res
        

