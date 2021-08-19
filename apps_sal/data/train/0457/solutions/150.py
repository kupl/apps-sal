class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(maxsize=None)
        def giveChange(target):
            if target == 0:
                return 0
            if target < 0:
                return -1
            minForTarget = None
            for coin in coins:
                result = giveChange(target - coin)
                if result != -1:
                    minForTarget = result + 1 if not minForTarget else min(result + 1, minForTarget)
            return minForTarget or -1
        return giveChange(amount)
