class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if nums[-1] != 0:
            nums.append(0)
        n = len(nums)
        first_0 = -1
        last_0 = -1
        cnt_neg = 0
        first_neg = -1
        last_neg = -1
        res = 0
        for i, e in enumerate(nums):
            if e < 0:
                cnt_neg += 1
                if first_neg == -1:
                    first_neg = i
                last_neg = i
            elif e == 0:
                last_0 = i
                if cnt_neg % 2 == 0:
                    res = max(res, last_0 - first_0 - 1)
                else:
                    res = max(res, last_neg - first_0 - 1, last_0 - first_neg - 1)
                cnt_neg = 0
                first_0 = last_0
                first_neg = -1
        return res
