class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}

        def dfs(i, bob):
            if (i, bob) in memo:
                return memo[i, bob]
            if i >= n:
                return 0
            ans = float('inf') if bob else float('-inf')
            for x in [1, 2, 3]:
                sub = dfs(i + x, 1 - bob)
                if bob:
                    ans = min(ans, sub)
                else:
                    ans = max(ans, sub + sum(stoneValue[i:i + x]))
            memo[i, bob] = ans
            return ans
        dfs(0, 0)
        dfs(0, 1)
        if memo[0, 1] == memo[0, 0]:
            return 'Tie'
        return 'Bob' if memo[0, 1] > memo[0, 0] else 'Alice'
