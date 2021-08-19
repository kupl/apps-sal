import heapq
from collections import defaultdict, Counter


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        mod_dic = defaultdict(list)    # Hash table: 1->[1, 7, 10...]
        for num in nums:
            mod_dic[num % 3].append(num)
        print(mod_dic)

        if sum_ % 3 == 0:
            return sum_

        if sum_ % 3 == 1:
            sum1 = -float('inf')
            sum2 = -float('inf')
            if 1 in mod_dic:
                sum1 = sum_ - min(mod_dic[1])
            if 2 in mod_dic and len(mod_dic[2]) >= 2:
                min_mod2, second_min_mod2 = heapq.nsmallest(2, mod_dic[2])
                sum2 = sum_ - min_mod2 - second_min_mod2
            return max(sum1, sum2)

        if sum_ % 3 == 2:
            sum1 = -float('inf')
            sum2 = -float('inf')
            if 2 in mod_dic:
                sum2 = sum_ - min(mod_dic[2])
            if 1 in mod_dic and len(mod_dic[1]) >= 2:
                min_mod1, second_min_mod1 = heapq.nsmallest(2, mod_dic[1])
                sum1 = sum_ - min_mod1 - second_min_mod1
            return max(sum1, sum2)
