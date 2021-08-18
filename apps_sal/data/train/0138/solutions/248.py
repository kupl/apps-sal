class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        neg = [0] * n
        pos = [0] * n

        if nums[0] < 0:
            neg[0] = 1
        elif nums[0] > 0:
            pos[0] = 1
        for i in range(1, n):
            val = nums[i]
            if val > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = (neg[i - 1] + 1) if neg[i - 1] != 0 else 0
            elif val < 0:
                pos[i] = (neg[i - 1] + 1) if neg[i - 1] != 0 else 0
                neg[i] = pos[i - 1] + 1
            else:
                pos[i] = 0
                neg[i] = 0
            print((pos[i], neg[i]))
        return max(pos)
