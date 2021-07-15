class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def max_len(i, j):
            if i > j:
                return 0
            res = 1
            for k in range(i, j+1):
                res *= nums[k]
            if res > 0:
                return j - i + 1
            l = i
            r = j
            while nums[l] > 0:
                l += 1
            while nums[r] > 0:
                r -= 1
            return max(j-l, r-i)
        prev = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(res, max_len(prev, i-1)) 
                prev = i+1
        res = max(res, max_len(prev, len(nums) -1))
        return res
