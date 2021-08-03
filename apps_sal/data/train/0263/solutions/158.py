class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0
        dic = {0: (4, 6),
               1: (8, 6),
               2: (7, 9),
               3: (4, 8),
               4: (3, 9, 0),
               5: (),
               6: (1, 7, 0),
               7: (2, 6),
               8: (1, 3),
               9: (2, 4)}
        dp = [1] * 10
        for _ in range(n - 1):
            new = [0] * 10
            for i in range(10):
                for nei in dic[i]:
                    new[i] += dp[nei]
            dp = new

        return sum(dp) % (10**9 + 7)
