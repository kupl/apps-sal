from collections import defaultdict


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        dp = defaultdict(list)
        res = [(0, -1)]
        tmp_sum = 0

        for i, val in enumerate(nums):

            tmp_sum += val

            if tmp_sum - target == 0 and i > res[-1][1]:
                res.append((0, i))
                tmp_sum = 0
            else:
                if tmp_sum - target in dp and dp[tmp_sum - target][-1] >= res[-1][1]:
                    res.append((0, i))
                    tmp_sum = 0

            dp[tmp_sum].append(i)

        return len(res) - 1
