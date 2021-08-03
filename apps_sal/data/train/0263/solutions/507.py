class Solution:
    def knightDialer(self, N: int) -> int:
        total = 0
        places = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        if N == 1:
            return 10
        dp = [1] * 10
        for i in range(2, N + 1):
            tmp = copy.deepcopy(dp)
            for i in range(0, 10):
                if i != 5:
                    vals = places.get(i)
                    new_tot = 0
                    for v in vals:
                        new_tot += dp[v]
                    tmp[i] = new_tot
            dp = copy.deepcopy(tmp)
        ans = 0
        for d in dp:
            ans += d
        return (ans - 1) % (10**9 + 7)
