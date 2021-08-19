import copy
from collections import defaultdict
from typing import List


class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        for v in rods:
            dp_ = copy.deepcopy(dp)
            for (diff, max_v) in list(dp.items()):
                dp_[diff + v] = max(dp_[diff + v], dp[diff])
                dp_[abs(diff - v)] = max(dp_[abs(diff - v)], max_v + min(diff, v))
            dp = dp_
        return dp[0]
