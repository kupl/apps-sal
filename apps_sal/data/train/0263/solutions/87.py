class Solution:
    def knightDialer(self, n: int) -> int:
        possible_paths = {1: [6, 8], 2: [7, 9], 3: [4,8], 4: [0, 3, 9], 5: [],
                          6: [0, 1,7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        dp = [1] * 10
        for i in range(n-1):
            temp = [0] * 10
            for start_num in range(10):
                for target_num in possible_paths[start_num]:
                    temp[target_num] += dp[start_num]
            dp = temp

        return sum(dp) % (7 + 10**9)
