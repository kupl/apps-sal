def prev(x, day, dp):
    ans = 0
    for i in day:
        if i <= x:
            ans = dp[i]
        else:
            break
    return ans


class Solution:
    def mincostTickets(self, day: List[int], cos: List[int]) -> int:
        dp = [10000000] * (370)
        tmp = [0] * 32
        tmp[1] = cos[0]
        tmp[7] = cos[1]
        tmp[30] = cos[2]
        day.sort()
        n = len(day)
        for i in range(n):
            d = day[i]
            for j in [1, 7, 30]:
                ab = prev(max(0, d - j), day, dp) + tmp[j]
                dp[d] = min(dp[d], ab)
        return dp[day[-1]]
