class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp_pos = [0] * (n + 1)
        dp_neg = [0] * (n + 1)

        result = 0
        for i in range(1, n + 1):
            if nums[i - 1] == 0:
                dp_pos[i] = 0
                dp_neg[i] = 0
            elif nums[i - 1] > 0:
                dp_pos[i] = 1 + dp_pos[i - 1]

                if dp_neg[i - 1] > 0:
                    dp_neg[i] = 1 + dp_neg[i - 1]
                else:
                    dp_neg[i] = 0
            else:
                if dp_neg[i - 1] > 0:
                    dp_pos[i] = 1 + dp_neg[i - 1]
                else:
                    dp_pos[i] = 0

                dp_neg[i] = 1 + dp_pos[i - 1]

            result = max(result, dp_pos[i])

        return result
