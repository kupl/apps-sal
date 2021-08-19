class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        ary = [amount + 1] * (amount + 1)
        ary[0] = 0
        for i in range(1, len(ary)):
            for coin in coins:
                if i - coin < 0:
                    continue
                ary[i] = min(ary[i], ary[i - coin] + 1)
        return ary[amount] if ary[amount] < amount + 1 else -1
