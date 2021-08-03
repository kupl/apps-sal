class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        piles = stoneValue
        n = len(piles)
        sums = 0
        for pile in piles:
            sums += pile

        def rec_max(i, n, sums):
            if i == n:
                return 0
            if i in dp:
                return dp[i][0]
            m = min(3, n - i)
            res_sum = float('-inf')
            res_gap = float('-inf')
            remains = sums
            for x in range(m):
                remains -= piles[i + x]
                other = rec_max(i + x + 1, n, remains)
                res = sums - other
                gap = res - other
                if gap > res_gap:
                    res_gap = gap
                    res_sum = res
            dp[i] = res_sum, res_gap
            return res_sum
        rec_max(0, n, sums)
        res = dp[0][1]
        if res < 0:
            return 'Bob'
        elif res > 0:
            return 'Alice'
        else:
            return 'Tie'
