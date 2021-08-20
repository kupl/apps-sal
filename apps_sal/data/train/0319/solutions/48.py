class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        (p1, p2, p3) = (0, 0, 0)
        post_sum = 0
        for i in range(len(stoneValue) - 1, -1, -1):
            val = stoneValue[i]
            post_sum += val
            best = post_sum - min([p1, p2, p3])
            (p1, p2, p3) = (best, p1, p2)
        if p1 > post_sum - p1:
            return 'Alice'
        elif p1 < post_sum - p1:
            return 'Bob'
        else:
            return 'Tie'

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        total = [0] * (len(stoneValue) + 4)
        for i in range(len(stoneValue) - 1, -1, -1):
            total[i] = total[i + 1] + stoneValue[i]
        dp = [0] * len(total)
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i] = total[i] - min(dp[i + 1:i + 4], default=0)
        alice = dp[0]
        bob = total[0] - alice
        if alice > bob:
            return 'Alice'
        elif alice < bob:
            return 'Bob'
        else:
            return 'Tie'
