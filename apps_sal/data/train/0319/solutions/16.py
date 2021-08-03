class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # def pick(player, stones):
        #     if len(stones) == 0:
        #         return 0
        #     if player == 1:
        #         return max(
        #             [stones[0] + pick(2,stones[1:]),
        #              sum(stones[:2]) + pick(2,stones[2:]),
        #              sum(stones[:3]) + pick(2,stones[3:])
        #             ])
        #     else:
        #         return min(
        #             [-stones[0] + pick(1,stones[1:]),
        #              -sum(stones[:2]) + pick(1,stones[2:]),
        #              -sum(stones[:3]) + pick(1,stones[3:])
        #             ])
        # ans = pick(1,stoneValue)
        # if ans == 0:
        #     return 'Tie'
        # elif ans < 0:
        #     return 'Bob'
        # else:
        #     return 'Alice'
        dp = [0] * (len(stoneValue) + 1)
        for i in range(len(stoneValue) - 1, -1, -1):
            take = 0
            dp[i] = -float('inf')
            for k in range(3):
                if i + k >= len(stoneValue):
                    continue
                take += stoneValue[i + k]
                dp[i] = max(dp[i], take - dp[i + k + 1])

        if dp[0] < 0:
            return 'Bob'
        if dp[0] > 0:
            return 'Alice'
        return 'Tie'
