import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        best_so_far = math.inf
        
        def rec(C, A, used):
            nonlocal best_so_far
            if A == 0:
                best_so_far = min(best_so_far, used)            
            elif C:
                for i in range(A//C[-1], -1, -1):
                    if (best_so_far - used) * C[-1] >= A:
                        rec(C[:-1], A - i*C[-1], used + i)
                    
        rec(coins, amount, 0)
        return best_so_far if best_so_far != math.inf else -1

