from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur = best = idx = 0
        best_idx = None
        waiting = 0
        capacity = 4

        while waiting or idx < len(customers):
            # Add new waiting customers, put passengers on ride, remove passengers from waiting.
            if idx < len(customers):
                waiting += customers[idx]
            
            passengers = min(waiting, capacity)
            waiting -= passengers

            # Update money.
            cur += (passengers * boardingCost) - runningCost

            if cur > best:
                best_idx = idx + 1
                best = cur  
            
            idx += 1
            

        if best_idx is None:
            best_idx = -1

        return best_idx
