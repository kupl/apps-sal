class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        pos = 0
        neg = 0
        left, right = -1, -1
        prev = -1
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                if cnt > 0 and neg % 2 == 0:
                    res = max(res, i - prev - 1)
                elif cnt > 0 and neg % 2 == 1:
                    res = max(res, i - left - 1, right - prev - 1)
                cnt = 0
                neg = 0
                prev = i
                left, right = prev, prev
                continue
            if nums[i] < 0:
                neg += 1
                if left == prev:
                    left = i
                right = i
                cnt += 1
            elif nums[i] > 0:
                cnt += 1
            if neg % 2 == 0:
                res = max(res, i - prev)
            else:
                res = max(res, i - left, right - prev - 1)
        return res
