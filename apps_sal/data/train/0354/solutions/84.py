class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 7 + 1e9
        @lru_cache(maxsize=None)
        def helper(idx, roll, turn):
            if roll > rollMax[idx]:
                return 0

            if turn == n:
                return 1

            result = 0
            if idx == -1:
                for i in range(len(rollMax)):
                    result = (result + helper(i, 1, turn + 1)) % MOD
            else:
                for i in range(len(rollMax)):
                    if i == idx:
                        result = (result + helper(i, roll + 1, turn + 1)) % MOD
                    else:
                        result = (result + helper(i, 1, turn + 1)) % MOD
            return result

        return int(helper(-1, 0, 0) % MOD)
