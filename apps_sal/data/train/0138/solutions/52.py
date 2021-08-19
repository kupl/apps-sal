class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        pos = 0
        neg = 0
        max_pos = 0
        curr = True
        for i in range(len(nums)):
            # print(nums[i])

            if nums[i] > 0:
                pos += 1
                if neg != 0:
                    neg += 1

            elif nums[i] < 0:
                old_pos = pos
                if neg != 0:
                    pos = neg + 1
                else:
                    pos = 0
                neg = old_pos + 1

            else:
                neg = 0
                pos = 0

            max_pos = max(pos, max_pos)
            # print(pos, max_pos,neg)

        return max_pos
