class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0] * (max(rollMax) + 1) for x in range(7)] for x in range(n + 1)]

        def dfs(roll, prev, count):

            if roll == 0:
                return 1

            if dp[roll][prev][count] != 0:
                return dp[roll][prev][count]

            result = 0
            for x in range(1, 7):
                if x == prev:
                    if count < rollMax[x - 1]:
                        result += dfs(roll - 1, x, count + 1)
                else:
                    result += dfs(roll - 1, x, 1)

            dp[roll][prev][count] = result
            return result

        return dfs(n, 0, 0) % 1000000007
