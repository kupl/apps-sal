class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        result = 0
        for r in [list(range(0, len(nums))), list(range(len(nums) - 1, -1, -1))]:
            cur_len = 0
            cur_sign = 1
            for i in r:
                if nums[i] > 0:
                    cur_len += 1
                    result = max(result, cur_sign * cur_len)
                elif nums[i] == 0:
                    cur_len = 0
                    cur_sign = 1
                else:
                    cur_len += 1
                    cur_sign = -cur_sign
                    result = max(result, cur_sign * cur_len)
        return result
