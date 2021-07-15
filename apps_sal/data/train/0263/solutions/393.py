import numpy as np

class Solution:
    # Time: O(N), Space: O(N).
    def knightDialer(self, N: int) -> int:
        goto = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }
        # We can build backwards...
        # With x moves left how many numbers numbers can you form from i.
        # For x = 0, 1. 
        
        # Shape (10, N).
        # dp[p, i] = on position p, with i move lefts, how many moves
        # can the knight make.
        dp = np.zeros((10, N)).astype(int)
        
        # With 0 moves left you can only make 1 number. 
        dp[:, 0] = 1
        
        for c in range(1, N):
            for p in range(10):
                for next_vals in goto[p]:
                    dp[p, c] += dp[next_vals, c - 1] % (10**9 + 7)
        
        return int(sum(dp[:, N - 1])) % (10**9 + 7)
