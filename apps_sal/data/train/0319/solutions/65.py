class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @lru_cache(None)
        def dp(cur):
            if cur >= n:
                return 0, 0
            first, second = -math.inf, -math.inf
            for i in range(1, 4):
                first_tmp, second_tmp = dp(cur + i)
                if first < second_tmp + sum(stoneValue[cur:cur + i]):
                    first = second_tmp + sum(stoneValue[cur:cur + i])
                    second = first_tmp
            return first, second
        alice, bob = dp(0)
        if alice > bob:
            return 'Alice'
        elif alice < bob:
            return 'Bob'
        else:
            return 'Tie'
