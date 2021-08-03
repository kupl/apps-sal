class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        x = 1
        s = []
        st = set()
        dp = [False] * (n + 1)
        while x * x <= n:
            s.append(x * x)
            st.add(x * x)
            dp[x * x] = True
            x += 1
        if n in s:
            return True
        for i in range(1, n + 1):
            if dp[i] == False:
                start = 0
                while start < len(s) and i - s[start] > 0:
                    if dp[i - s[start]] == False:
                        dp[i] = True
                        break
                    start += 1
        return dp[n]
