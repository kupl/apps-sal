class Solution:
    # 5 can only show up as the last number
    def knightDialer(self, n: int) -> int:
        from collections import defaultdict
        dct = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        dp = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 0: 1}   # number: curr_sum
        n -= 1

        while n > 0:
            new_dp = defaultdict(int)
            for num1 in dp:
                for num2 in dct[num1]:
                    new_dp[num2] += dp[num1]
            dp = new_dp
            n -= 1

        ans = 0
        for key in dp:
            ans += dp[key]
        return ans % (10**9 + 7)
