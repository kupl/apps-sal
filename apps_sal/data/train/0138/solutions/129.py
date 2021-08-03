class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos = [0 for x in range(n)]
        neg = [0 for x in range(n)]

        if nums[0] > 0:
            pos[0] = 1
        if nums[0] < 0:
            neg[0] = 1

        ret = pos[0]
        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                neg[i] = pos[i - 1] + 1
                pos[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
            else:
                continue
            ret = max(ret, pos[i])
        return ret
