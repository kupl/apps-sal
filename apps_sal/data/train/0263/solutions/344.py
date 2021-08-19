MOVES = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]


class Solution:

    def knightDialer(self, N: int) -> int:
        memo = {}
        res = 0
        for i in range(10):
            res += self._dfs(i, N, memo)
        return res % (10 ** 9 + 7)

    def _dfs(self, curr, steps, memo):
        if steps == 1:
            return 1
        key = (curr, steps)
        if key in memo:
            return memo[key]
        memo[key] = 0
        for next_digit in MOVES[curr]:
            memo[key] += self._dfs(next_digit, steps - 1, memo)
        return memo[key]
