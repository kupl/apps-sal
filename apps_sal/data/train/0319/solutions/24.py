class Solution:

    def stoneGameIII(self, stones):
        total = sum(stones)
        alice_value = self._dfs(stones, 0, {})
        if alice_value > 0:
            return 'Alice'
        elif alice_value < 0:
            return 'Bob'
        return 'Tie'

    def _dfs(self, stones, start, memo):
        if start >= len(stones):
            return 0
        if start in memo:
            return memo[start]
        res = -2 ** 31
        curr_total = 0
        for i in range(start, min(start + 3, len(stones))):
            curr_total += stones[i]
            next_player_values = self._dfs(stones, i + 1, memo)
            res = max(res, curr_total - next_player_values)
        memo[start] = res
        return res
