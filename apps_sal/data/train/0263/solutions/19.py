class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4, 6],[6, 8],[7, 9],[4, 8]
                 ,[0, 3, 9],[],[0, 1, 7]
                 ,[2, 6],[1, 3],[2, 4]]
        dp = [1] * 10
        for _ in range(n-1):
            dp2 = [0] * 10
            for i, cnt in enumerate(dp):
                for nxt in moves[i]:
                    dp2[nxt] += cnt
            dp = dp2
        return sum(dp) % (10**9 + 7)
