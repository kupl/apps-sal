class Solution:
    def knightDialer(self, n: int) -> int:
        jump = {1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[],6:[0,1,7], 7:[6,2],8:[1,3],9:[4,2],0:[6,4]}
        dp = [1]*10
        for _ in range(n-1):
            new_dp = [0]*10
            for v in range(10):
                for u in jump[v]:
                    new_dp[v] += dp[u]
            dp = new_dp
        return sum(dp)%(10**9+7)
