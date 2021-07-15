class Solution:
    def knightDialer(self, n: int) -> int:
        # dp[i, j] = # of distinct phone numbers of length j that can be dialed starting at i
        # dp[i, 1] = 1
        # dp[i, j] = sum(dp[i-1, k]) where k are all the possible numbers the knight can jump to
        if n == 1:
            return 10
        possible_next_digits = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        dp = [1 for _ in range(10)]
        dp_next = [0 for _ in range(10)]

        for _ in range(n-1):
            for j in range(10):
                dp_next[j] = 0
                for digit in possible_next_digits[j]:
                    dp_next[j] += dp[digit]
            for j in range(10):
                dp[j] = dp_next[j]

        total = 0
        for num in dp:
            total += num
        return total % (10**9 + 7)

