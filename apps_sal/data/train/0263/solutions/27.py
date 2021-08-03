class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1 for _ in range(10)]
        BASE = 10**9 + 7
        data = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        for i in range(n - 1):
            dp_tmp = []
            for j in range(10):
                sum_tmp = 0
                for k in data[j]:
                    sum_tmp += (dp[k] % BASE)
                dp_tmp.append(sum_tmp % BASE)
            dp = dp_tmp

        return sum(dp) % BASE
