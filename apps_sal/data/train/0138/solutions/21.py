class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos_num = neg_num = res = 0
        for i, num in enumerate(nums):
            if num == 0:
                pos_num = neg_num = 0
            elif num > 0:
                neg_num = neg_num + 1 if neg_num else 0
                pos_num += 1
            else:
                cur_pos = pos_num
                pos_num = neg_num + 1 if neg_num else 0
                neg_num = cur_pos + 1
            res = max(res, pos_num)
        return res
