class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pos = [0] * (len(nums) + 1)
        neg = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            if n > 0:
                pos[i + 1] = pos[i] + 1
                if neg[i] != 0:
                    neg[i + 1] = neg[i] + 1
            elif n < 0:
                if neg[i] == 0:
                    neg[i + 1], pos[i + 1] = pos[i] + 1, 0
                else:
                    neg[i + 1], pos[i + 1] = pos[i] + 1, neg[i] + 1
            else:
                neg[i + 1] = pos[i + 1] = 0
        return max(pos)
