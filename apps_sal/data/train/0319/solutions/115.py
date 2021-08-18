class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        if not stoneValue:
            return 'Tie'

        pre_sum = [0 for _ in range(len(stoneValue) + 1)]
        for i in range(len(stoneValue)):
            pre_sum[i + 1] = pre_sum[i] + stoneValue[i]

        @lru_cache(None)
        def dfs(idx, player):
            if idx > len(stoneValue) - 1:
                return 0
            if player == 1:
                res = float('-inf')
                for i in range(1, 4):
                    if idx + i > len(stoneValue):
                        break
                    res = max(res, pre_sum[idx + i] - pre_sum[idx] + dfs(idx + i, -player))
            else:
                res = float('inf')
                for i in range(1, 4):
                    res = min(res, dfs(idx + i, -player))

            return res

        a_sum = dfs(0, 1)
        b_sum = pre_sum[-1] - a_sum

        if a_sum == b_sum:
            return 'Tie'
        elif a_sum > b_sum:
            return 'Alice'
        else:
            return 'Bob'
