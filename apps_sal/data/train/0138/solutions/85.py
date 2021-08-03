class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        N = len(nums)
        pos, neg = [0] * N, [0] * N
        if nums[0] > 0:
            pos[0] = 1
        if nums[0] < 0:
            neg[0] = 1
        res = pos[0]

        for i in range(1, N):
            if nums[i] > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
                neg[i] = pos[i - 1] + 1
            res = max(pos[i], res)
        return res
