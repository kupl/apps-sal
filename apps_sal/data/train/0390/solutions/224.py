class Solution:

    def winnerSquareGame(self, n):
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            iswin = False
            for k in range(1, int(sqrt(i)) + 1):
                if not dp[i - k * k]:
                    iswin = True
                    break
            dp[i] = iswin
        return dp[-1]

    def winnerSquareGame2(self, n):
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            iswin = False
            for k in range(1, int(sqrt(i)) + 1):
                if not dp[i - k * k]:
                    iswin = True
                    break
            dp[i] = iswin
        return dp[-1]

    def winnerSquareGame1(self, n: int) -> bool:

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
