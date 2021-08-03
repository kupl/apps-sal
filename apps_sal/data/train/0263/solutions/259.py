class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [6, 4]
        }
        p = 10**9 + 7

        dp = defaultdict(lambda: 1)
        for t in range(n - 1):
            for i in range(10):
                dp[i, t & 1] = sum(dp[j, (t + 1) & 1] for j in neighbors[i]) % p

        return sum(dp[i, n & 1] for i in range(10)) % p
