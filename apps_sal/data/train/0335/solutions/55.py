class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            cur = dp.copy()
            for (k, v) in dp.items():
                cur[k + rod] = max(v + rod, cur.get(k + rod, 0))
                cur[k - rod] = max(v, cur.get(k - rod, 0))
                cur[k] = max(v, cur.get(k, 0))
            dp = cur
        return dp[0]
