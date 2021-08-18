
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        remain = list(itertools.accumulate(stoneValue[::-1]))[::-1]

        @lru_cache(None)
        def dp(idx):
            if idx >= len(stoneValue):
                return 0
            return remain[idx] - min(dp(idx + i) for i in range(1, 4))

        first = dp(0)
        second = remain[0] - first
        return 'Alice' if first > second else 'Tie' if first == second else 'Bob'

    def stoneGameIII(self, stoneValue: List[int]) -> str:

        remain = list(itertools.accumulate(stoneValue[::-1]))[::-1]
        n = len(stoneValue)
        dp = [0] * (n + 4)

        for idx in range(n - 1, -1, -1):
            dp[idx] = remain[idx] - min(dp[idx + i] for i in range(1, 4))

        first = dp[0]
        second = remain[0] - first
        print([dp[i] for i in range(len(stoneValue))])
        return 'Alice' if first > second else 'Tie' if first == second else 'Bob'
