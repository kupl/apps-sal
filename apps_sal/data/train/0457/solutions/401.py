class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        res = amount // coins[-1] + 1

        def comb(cursum, num, index):
            nonlocal res
            if (amount - cursum) / coins[index] >= res - num:
                return
            for i in range(index, len(coins)):
                newsum = cursum + coins[i]
                if newsum == amount:
                    res = min(num + 1, res)
                    return
                elif newsum < amount:
                    comb(newsum, num + 1, i)
        comb(0, 0, 0)
        if res == amount // coins[-1] + 1:
            return -1
        return res
