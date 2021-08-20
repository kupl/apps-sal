class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        ownhat = {}
        n = len(hats)
        for i in range(n):
            hat = hats[i]
            for h in hat:
                if h in ownhat:
                    ownhat[h].append(i)
                else:
                    ownhat[h] = [i]
        dp = [[-1 for i in range(pow(2, n))] for i in range(41)]

        def dfs(ind, peoplemask, dp):
            if peoplemask == pow(2, n) - 1:
                return 1
            if ind > 40:
                return 0
            count = 0
            if dp[ind][peoplemask] != -1:
                return dp[ind][peoplemask]
            count = dfs(ind + 1, peoplemask, dp)
            if ind in ownhat:
                for people in ownhat[ind]:
                    if peoplemask & pow(2, people) == 0:
                        count = (count + dfs(ind + 1, peoplemask | pow(2, people), dp)) % (pow(10, 9) + 7)
            dp[ind][peoplemask] = count
            return count
        return dfs(1, 0, dp)
