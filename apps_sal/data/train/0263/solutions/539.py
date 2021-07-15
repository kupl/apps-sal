class Solution:
    def knightDialer(self, N: int) -> int:
        dp = [1] * 10
        MOD = 10 ** 9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        
        for hop in range(N - 1):
            new_dp = [0] * 10
            for num, count in enumerate(dp):
                for neigh in moves[num]:
                    new_dp[neigh] = (new_dp[neigh] + count) % MOD
            dp = new_dp
        
        return sum(dp) % MOD
