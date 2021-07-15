class Solution:
    def knightDialer(self, n: int) -> int:
        # dp(0, digit) = 0
        # dp(n steps, digit) = sum(dp(n - 1, f) for f in digit's friends)
        if n == 0:
            return 0
        
        friends = [0] * 10
        friends[0] = [4, 6]
        friends[1] = [6, 8]
        friends[2] = [7, 9]
        friends[3] = [8, 4]
        friends[4] = [0, 3, 9]
        friends[5] = []
        friends[6] = [0, 1, 7]
        friends[7] = [2, 6]
        friends[8] = [1, 3]
        friends[9] = [2, 4]
        
        dp = [[0 for _ in range(10)] for _ in range(n + 1)]
        dp[1] = [1] * 10
        for steps in range(2, n + 1):
            for digit in range(10):
                dp[steps][digit] = sum([dp[steps - 1][f] for f in friends[digit]]) % (10**9 + 7)
        
        return sum(dp[-1]) % (10**9 + 7)

