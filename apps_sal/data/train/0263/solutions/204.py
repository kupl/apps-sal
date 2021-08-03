class Solution:
    def knightDialer(self, n: int) -> int:
        moveable = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        MOD = 7 + 1e9

        @lru_cache(maxsize=None)
        def helper(step, num=-1):
            if step == n:
                return 1

            result = 0
            if num == -1:
                for i in range(10):
                    result = (result + helper(step + 1, i)) % MOD
            else:
                for move in moveable[num]:
                    result = (result + helper(step + 1, move)) % MOD
            return result

        return int(helper(0))
