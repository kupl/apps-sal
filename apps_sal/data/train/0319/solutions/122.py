class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        memo = {}

        def solve(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]
            ans, curr = -math.inf, 0
            for j in range(i, min(n, i + 3)):
                curr += stones[j]
                ans = max(ans, curr - solve(j + 1))
            memo[i] = ans
            return ans
        score = solve(0)
        if score > 0:
            return 'Alice'
        elif score < 0:
            return 'Bob'
        else:
            return 'Tie'
