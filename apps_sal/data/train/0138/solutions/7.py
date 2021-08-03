class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        plus, minus, res, c = 0, -1, 0, 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                if c % 2 == 1:
                    res = max(res, minus)
                else:
                    res = max(res, max(plus, minus))
                plus, minus, c = 0, -1, 0
            elif nums[i] > 0:
                if minus != -1:
                    minus += 1
                plus += 1
            else:
                c += 1
                minus += 1
                if c % 2 == 1:
                    res = max(res, max(minus, plus))
                plus += 1
        if c % 2 == 1:
            res = max(res, minus)
        else:
            res = max(res, max(plus, minus))
        return res
