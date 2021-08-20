class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for r in rods:
            newdp = collections.defaultdict(int)
            for d in dp:
                newdp[d + r] = max(newdp[d + r], dp[d] + r)
                newdp[d] = max(newdp[d], dp[d])
                newdp[d - r] = max(newdp[d - r], dp[d])
            dp = newdp
        return dp[0]
