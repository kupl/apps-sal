from collections import defaultdict


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for rod in rods:
            currents = collections.defaultdict(int)
            for diff in dp:
                currents[diff + rod] = max(dp[diff] + rod, currents[diff + rod])
                currents[diff] = max(dp[diff], currents[diff])
                currents[diff - rod] = max(dp[diff], currents[diff - rod])
            dp = currents

        return dp[0]
