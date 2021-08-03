class Solution:
    def knightDialer(self, N: int) -> int:
        #         MOD = 10**9 + 7
        #         # dp = [ [[0]*3 for _2 in range(4)]   for _ in range(N)]
        #         dp = [[0]*3 for _2 in range(4)]
        #         for i in range(4):
        #             for j in range(3):
        #                 if (i,j) in [(3,0),(3,2)]:
        #                     continue
        #                 dp[i][j] = 1

        #         for k in range(1,N):
        #             new_dp = [[0]*3 for _2 in range(4)]
        #             for i in range(3):
        #                 for j in range(i,3):
        #                     # print(i,j)
        #                     a = [[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1],
        #                          [i+1,j+2],[i-1,j+2],[i+1,j-2],[i-1,j-2]]
        #                     for p in a:
        #                         if not(0 <= p[0] < 4) or not(0 <= p[1] < 3):
        #                             continue
        #                         new_dp[i][j] += dp[p[0]][p[1]] % MOD
        #                         # new_dp[j][i] = new_dp[i][j]
        #             new_dp[1][0] = new_dp[1][2]
        #             new_dp[2][0] = new_dp[2][2]
        #             new_dp[2][1] = new_dp[0][1]
        #             i = 3
        #             j = 1
        #             new_dp[3][1] = (dp[1][2] + dp[1][0]) % MOD
        #             dp = new_dp
        #             # print(dp)

        #         s = 0
        #         # dp[3][0] = dp[N-1][3][2] = 0
        #         for i in dp:
        #             for j in i:
        #                 s += j % MOD
        #         return s % MOD

        cac = {}
        MOD = 10**9 + 7
        pmvs = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [4, 2]]

        def d(k, i):
            try:
                # 1/0
                return cac[(k, i)]
            except:
                pass
            if k == 0:
                return 1
            s = 0
            for j in pmvs[i]:
                s += d(k - 1, j) % MOD
            cac[(k, i)] = s % MOD
            return cac[(k, i)]
        ans = 0
        for i in range(10):
            ans += d(N - 1, i) % MOD
        return ans % MOD
