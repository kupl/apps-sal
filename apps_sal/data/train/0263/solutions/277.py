class Solution:
    def knightDialer(self, N: int) -> int:
        mapping = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        if N == 1:
            return 10
        dp = collections.defaultdict(int)
        for idx in range(10):
            if idx == 5:
                continue
            dp[idx] = 1
        while N > 1:
            next_dp = collections.defaultdict(int)
            for idx in range(10):
                if idx == 5:
                    continue
                for k in mapping[idx]:
                    next_dp[k] += dp[idx]
            N -= 1
            dp = next_dp
        return sum(dp.values()) % (10**9 + 7)
