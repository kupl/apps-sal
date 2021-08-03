class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        dp = [0] * (121)
        for i in ages:
            dp[i] += 1

        ans = 0
        mp = {}
        for i in range(15, 121):
            p = 0
            if dp[i] > 0:
                if i % 2 == 0:
                    Min = int((i / 2) + 8)
                else:
                    Min = int(math.ceil((i / 2) + 7))
                # Min=int(0.5*i+7)
                Max = i
                j = Min
                while j <= Max and j <= 120:
                    if j == i:
                        ans += dp[j] * (dp[j] - 1)
                        p += dp[j] * (dp[j] - 1)
                    else:
                        ans += dp[i] * dp[j]
                        p += dp[i] * dp[j]
                    j += 1

                mp[i] = p

        # print(mp)
        return ans
