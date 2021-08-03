class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dic = {0: 0}

        for num in nums:
            dic_new = {}

            for prev_remain, prev_sum in list(dic.items()):
                remain = (prev_remain + num) % 3
                dic_new[remain] = max(num + prev_sum, dic.get(remain, 0))

            for remain, sum_val in list(dic_new.items()):
                dic[remain] = max(sum_val, dic.get(remain, 0))

        return dic[0]
