class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * (n + 1) for _ in range(6)]
        for roll in range(1, n + 1):
            for face in range(6):
                if roll == 1:
                    dp[face][roll] = 1
                else:
                    for k in range(1, rollMax[face] + 1):
                        if roll - k < 0:
                            break
                        elif roll - k == 0:
                            dp[face][roll] += 1
                        else:
                            for l in range(6):
                                if l != face:
                                    dp[face][roll] += dp[l][roll - k]
        res = 0
        for i in range(6):
            res += dp[i][-1]
        return res % (10 ** 9 + 7)
