class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @lru_cache(maxsize=None)
        def solve(i: int) -> int:
            if i >= len(stoneValue):
                return 0
            res = -math.inf
            for stones in range(1, 4):
                curr_val = sum(stoneValue[i:i + stones]) + min(solve(i + stones + 1), solve(i + stones + 2), solve(i + stones + 3))
                res = max(res, curr_val)
            return res
        alice = solve(0)
        bob = sum(stoneValue) - alice
        if alice == bob:
            return 'Tie'
        elif alice > bob:
            return 'Alice'
        else:
            return 'Bob'
