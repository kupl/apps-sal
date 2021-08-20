from itertools import accumulate


class Solution:

    def stoneGameIII(self, sv: List[int]) -> str:
        m = len(sv)
        dp = [-sys.maxsize] * m
        dp.append(0)
        ps = list(accumulate(sv))
        sm = sum(sv)
        for i in range(m - 1, -1, -1):
            if i == m - 1:
                dp[i] = sv[i]
            elif i == m - 2:
                dp[i] = max(dp[i], sv[i] + (ps[-1] - ps[i] - dp[i + 1]))
                dp[i] = max(dp[i], sv[i] + sv[i + 1])
            else:
                dp[i] = max(dp[i], sv[i] + (ps[-1] - ps[i] - dp[i + 1]))
                dp[i] = max(dp[i], sv[i] + sv[i + 1] + (ps[-1] - ps[i + 1] - dp[i + 2]))
                dp[i] = max(dp[i], sv[i] + sv[i + 1] + sv[i + 2] + (ps[-1] - ps[i + 2] - dp[i + 3]))
        if dp[0] * 2 == sm:
            return 'Tie'
        if dp[0] * 2 > sm:
            return 'Alice'
        return 'Bob'
