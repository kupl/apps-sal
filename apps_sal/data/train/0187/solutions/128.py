class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        queue = collections.deque()
        waiting = 0
        profit = float('-inf')
        cur = 0
        rounds = 1
        members = 0
        final_rounds = 0
        
        for c in customers:
            waiting += c
            
            new = min(4, waiting)
            members += new
            waiting -= new
            
            cur = boardingCost * members - runningCost * rounds
            if cur > profit:
                profit = cur
                final_rounds = rounds
            rounds += 1
        
        while waiting:
            new = min(4, waiting)
            members += new
            waiting -= new
            
            cur = boardingCost * members - runningCost * rounds
            if cur > profit:
                profit = cur
                final_rounds = rounds
            rounds += 1

        return final_rounds if profit > 0 else -1
