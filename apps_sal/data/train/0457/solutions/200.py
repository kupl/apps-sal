class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        D = [0] * (amount + 1)

        def helper(rem):
            nonlocal D
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if D[rem] != 0:
                return D[rem]
            minn = float('inf')
            for coin in coins:
                res = helper(rem - coin)
                if res >= 0 and res < minn:
                    minn = res + 1
            if minn == float('inf'):
                D[rem] = -1
            else:
                D[rem] = minn
            return D[rem]
        return helper(amount)
