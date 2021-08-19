class Solution:

    def knightDialer(self, N: int) -> int:
        total = 0
        places = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        if N == 1:
            return 10
        dp = [1] * 10
        for i in range(2, N + 1):
            tmp_dp = [0] * 10
            for i in range(0, 10):
                if i != 5:
                    neighbors = places.get(i)
                    curr = 0
                    for n in neighbors:
                        curr += dp[n]
                    tmp_dp[i] = curr
            dp = copy.deepcopy(tmp_dp)
        return sum(dp) % (10 ** 9 + 7)
