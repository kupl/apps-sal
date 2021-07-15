class Solution:
    def longestSubarray(self, nums):
        n = len(nums)
        last_zero = None
        last_one = None
        cnt = 0
        res = 0
        for i in range(n):
            if nums[i] == 1:
                if last_one is None:
                    last_one = i
                cnt += 1 
            else:
                if last_zero is None:
                    last_zero = i
                else:
                    last_one = last_zero + 1
                    last_zero = i
                    cnt = i - last_one
            res = max(res, cnt)
        if res == n:
            return n - 1
        return res    
