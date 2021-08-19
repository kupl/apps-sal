class Solution:

    def knightDialer(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        reach = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        memo = {}

        def helper(num, steps):
            if (num, steps) in memo:
                return memo.get((num, steps))
            if steps == 0:
                memo[num, steps] = 1
                return memo.get((num, steps))
            res = 0
            for next_no in reach[num]:
                res += helper(next_no, steps - 1)
            res = res % MOD
            memo[num, steps] = res
            return res
        result = 0
        for pos in range(0, 10):
            result += helper(pos, N - 1)
        return result % MOD
