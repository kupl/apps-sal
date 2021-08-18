class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        prefix_sum = 0

        dict_odds = {0: 1}

        rs = 0

        for i, num in enumerate(nums):
            if num % 2 == 1:
                prefix_sum += 1

            if prefix_sum not in dict_odds:
                dict_odds[prefix_sum] = 1
            else:
                dict_odds[prefix_sum] = dict_odds[prefix_sum] + 1

            if (prefix_sum - k) in dict_odds:
                rs += dict_odds[(prefix_sum - k)]

        return rs
