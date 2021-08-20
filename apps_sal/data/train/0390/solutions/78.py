class Solution:

    def winnerSquareGame2(self, n):
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all((dp[i - k * k] for k in range(1, int(i ** 0.5) + 1)))
        return dp[-1]

    def winnerSquareGame(self, n: int) -> bool:
        cache = dict()

        def solve(s):
            if s in cache:
                return cache[s]
            if s == 0:
                cache[s] = False
                return False
            if pow(int(sqrt(s)), 2) == s:
                cache[s] = True
                return True
            iswin = False
            for k in range(1, int(sqrt(s)) + 1):
                if not solve(s - k * k):
                    iswin = True
                    break
            cache[s] = iswin
            return iswin
        return solve(n)
