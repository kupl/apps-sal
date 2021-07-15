class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = []
        product = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                product = product
                dp.append(product)
            elif nums[i] < 0:
                product = -product
                dp.append(product)
            else:
                product = 1
                dp.append(0)
        
        print(dp)
        res = 0
        d = {1:0, 0:float('inf'), -1:float('inf')}
        
        if nums[0] == 0:
            d[1] = float('inf')
        
        for i, p in enumerate(dp):
            if p == 1:
                d[1] = min(d[1], i)
                res = max(res, i - d[1] + 1)
            elif p == -1:
                d[-1] = min(d[-1], i)
                res = max(res, i - d[-1])
            else:
                d[1] = i + 1
                d[-1] = float('inf')
        
        return res

