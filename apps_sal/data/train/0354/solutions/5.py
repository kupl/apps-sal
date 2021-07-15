class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = pow(10, 9) + 7
        dp = [[1] + [0 for _ in range(14)] for _ in range(6)]
        
        for _ in range(n - 1):
            dp1 = [[0 for _ in range(15)] for _ in range(6)]
            sums = [sum(s) for s in dp]
            for num in range(6):
                dp1[num][0] = sum(sums[0:num]) + sum(sums[num + 1:])
                for x in range(1, 15):
                    if x > rollMax[num] - 1: break
                    dp1[num][x] = dp[num][x - 1]
            
            dp = dp1
            
        return sum([sum(l) for l in dp]) % mod
