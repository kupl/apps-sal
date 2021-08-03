class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = collections.defaultdict(lambda: 0)
        dp[0] = 0
        for rod in rods:
            nextlevel = collections.defaultdict(lambda: 0)
            for key, val in list(dp.items()):
                nextlevel[key + rod] = max(nextlevel[key + rod], val + rod)
                nextlevel[key] = max(nextlevel[key], val)
                nextlevel[key - rod] = max(nextlevel[key - rod], val + rod)
            dp = nextlevel
        return dp[0] // 2
