class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        a = [amount + 1] * (amount + 1)
        a[0] = 0

        for i in range(1, amount + 1):
            mlist = [a[i - c] for c in coins if i - c >= 0]
            if len(mlist) > 0:
                a[i] = 1 + min(mlist)

        print(a)
        if a[amount] > amount:
            return -1
        else:
            return a[amount]
