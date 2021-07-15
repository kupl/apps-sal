class Solution:
    def knightDialer(self, n: int) -> int:
        # time O(n); space O(1)
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[], [1,7,0],[2,6],[1,3],[2,4]]
        
        dp = [1] * 10
        for hop in range(n-1):
            new_dp = [0] * 10
            for node, cnt in enumerate(dp):
                for nei in moves[node]:
                    new_dp[nei] += cnt
            dp = new_dp
        
        return sum(dp) % (10**9+7)
