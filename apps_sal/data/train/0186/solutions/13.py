class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0]
        for i in range(1, target + 1):
            best = 0
            for (j, c) in enumerate(cost):
                if i - c < 0:
                    continue
                if dp[i - c] == 0 and i != c:
                    continue
                best = max(best, 10 * dp[i - c] + j + 1)
            dp.append(best)
        return str(dp[-1])
        '\n        pairs = [(c,-i-1) for i,c in enumerate(cost)]\n        #pairs.sort()\n        out = 0\n        def dfs(target, painted) -> bool:\n            nonlocal out\n            if target == 0:\n                out = max(out,int(painted))\n                return\n            if target < 0:\n                return\n            for i in range(9):\n                dfs(target - pairs[i][0], painted + str(-pairs[i][1]))\n        dfs(target,"")\n        return str(out)\n        '
