class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        n = len(nums)

        pos, neg = [0] * len(nums), [0] * len(nums)

        if nums[0] > 0:
            pos[0] = 1
        if nums[0] < 0:
            neg[0] = 1

        ans = pos[0]
        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = 1 + neg[i - 1] if neg[i - 1] else 0

            elif nums[i] < 0:
                neg[i] = pos[i - 1] + 1
                pos[i] = 1 + neg[i - 1] if neg[i - 1] else 0

            ans = max(ans, pos[i])

        return ans
