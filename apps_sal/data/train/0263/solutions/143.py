class Solution:
    def knightDialer(self, n: int) -> int:     
        graph = {
            0: [4, 6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4:[9, 3, 0],
            5: [],
            6: [7, 1, 0], 
            7: [6, 2],
            8: [1, 3],
            9: [2,4]
        }
        
        prev_dp = [1] * 10
        for i in range(n-1):
            dp = [0] * 10
            for j in range(10):
                dp[j] = sum(prev_dp[k] for k in graph[j]) % (10**9 + 7)
            prev_dp = dp
        return sum(prev_dp) % (10**9 + 7)
