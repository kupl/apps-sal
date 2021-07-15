class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target+1)
        for i in range(1, target+1):
            dp[i] = float('inf')           
            j = 1
            m = 1
            while j < i:
                p = 0
                q = 0
                while q < j:
                    dp[i] = min(dp[i], dp[i-(j-q)] + m + 1 + p + 1)
                    p += 1
                    q = (1<<p) - 1
                m += 1
                #print('j', m>>1-1, m, (m<<1) - 1)
                j = (1<<m) - 1
            #print(i, j)
            # if i == 6:
            #     print(m, dp[j-1])
            dp[i] = min(dp[i], m if j == i else m + 1 + dp[j-i])
        return dp[target]

