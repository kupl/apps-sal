class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = [0 for _ in range(len(nums))]  # pos[i] is number of consecutive numbers with pos product up to i
        neg = [0 for _ in range(len(nums))]  # neg[i] is number of consecutive numbers with neg product up to i
        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1

        out = pos[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                neg[i] = 1 + neg[i - 1] if neg[i - 1] else 0
            elif nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] else 0
                neg[i] = 1 + pos[i - 1]
            out = max(out, pos[i])

        return out
