class Solution:
    def knightDialer(self, N: int) -> int:
        # Space O(10)
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        dp = [1] * 10
        MOD = 10**9 + 7
        for i in range(N - 1):
            next_dp = [0] * 10
            for j in range(10):
                for next_digit in moves[j]:
                    next_dp[j] = (next_dp[j] + dp[next_digit]) % MOD
            dp = next_dp
        return sum(dp) % MOD
        
        # space O(10 * N)
        # mapping = {1:[6,8], 
        #            2:[7,9], 
        #            3:[4,8], 
        #            4:[3,9,0],
        #            5:[],
        #            6:[1,7,0],
        #            7:[2,6], 
        #            8:[1,3], 
        #            9:[2,4], 
        #            0:[4,6]}
        # dp = [[0] * 10 for _ in range(N)]
        # dp[0] = [1] * 10
        # for i in range(1, N):
        #     for j in range(10):
        #         for next_digit in mapping[j]:
        #             dp[i][j] += dp[i - 1][next_digit]
        # return sum(dp[-1]) % (10**9 + 7)

