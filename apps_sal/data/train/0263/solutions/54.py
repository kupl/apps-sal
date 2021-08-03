class Solution:
    def knightDialer(self, n: int) -> int:
        nxt = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp0 = [1] * 10

        for _ in range(1, n):
            dp1 = [0] * 10
            for i in range(10):
                for j in nxt[i]:
                    dp1[j] += dp0[i]
            dp0[:] = dp1[:]

        return sum(dp0) % (10**9 + 7)
