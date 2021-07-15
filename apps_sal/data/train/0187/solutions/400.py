class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxProfit = - 1
        idx = -1
        prevWaiting = 0
        runningProfit = 0
        # print(\"------\")
        i = 0
        while i < len(customers) or prevWaiting > 0:
            val = customers[i] if i < len(customers) else 0
            boarded = min(4, prevWaiting + val)
            runningProfit += boarded * boardingCost - runningCost
            # print(f\"{i} running profit = {runningProfit}\")
            if runningProfit > maxProfit:
                maxProfit = runningProfit
                idx = i
            
            prevWaiting = max(prevWaiting + val - 4, 0)
            i += 1
        
        return idx if idx == -1 else idx + 1

