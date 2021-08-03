class Solution:
    def knightDialer(self, n: int) -> int:

        mod = 10**9 + 7
        next_dic = {}
        next_dic[1] = [8, 6]
        next_dic[2] = [7, 9]
        next_dic[3] = [4, 8]

        next_dic[4] = [3, 9, 0]
        next_dic[5] = []
        next_dic[6] = [7, 1, 0]

        next_dic[7] = [2, 6]
        next_dic[8] = [3, 1]
        next_dic[9] = [2, 4]

        next_dic[0] = [6, 4]

        dp = [1] * 10
        for i in range(n - 1):
            dp_new = [0] * 10
            for i in range(10):
                for move in next_dic[i]:
                    dp_new[move] = (dp_new[move] + dp[i]) % mod
            del dp
            dp = dp_new
        return sum(dp) % mod
