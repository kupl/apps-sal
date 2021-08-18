class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0]
        for i in range(1, target + 1):
            best = 0
            for j, c in enumerate(cost):
                if i - c < 0:
                    continue
                if dp[i - c] == 0 and i != c:
                    continue
                best = max(best, 10 * dp[i - c] + j + 1)
            dp.append(best)
        return str(dp[-1])

        '''
        pairs = [(c,-i-1) for i,c in enumerate(cost)]
        out = 0
        def dfs(target, painted) -> bool:
            nonlocal out
            if target == 0:
                out = max(out,int(painted))
                return
            if target < 0:
                return
            for i in range(9):
                dfs(target - pairs[i][0], painted + str(-pairs[i][1]))
        dfs(target,\"\")
        return str(out)
        '''
