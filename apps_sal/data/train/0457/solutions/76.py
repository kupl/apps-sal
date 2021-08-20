class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        cnt = 0
        toCheck = {amount}
        while toCheck:
            cnt += 1
            tmp = set()
            for x in toCheck:
                for y in coins:
                    if y == x:
                        return cnt
                    if y > x:
                        break
                    tmp.add(x - y)
            if not tmp:
                return -1
            toCheck = tmp

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            dp[i] = min((dp[i - c] if i - c >= 0 else float('inf') for c in coins)) + 1
        return dp[-1] if dp[-1] != float('inf') else -1
