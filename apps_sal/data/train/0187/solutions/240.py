class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        extra = 0
        count = 0
        total = 0
        profit = 0
        round = 0
        for i in range(0,len(customers)):
            customers[i] += extra
            if customers[i] > 4:
                extra = customers[i]-4
                total += 4
                count += 1
            else:
                extra = 0
                total += customers[i]
                count += 1
            if total * boardingCost - runningCost * count > profit:
                    profit = total * boardingCost - runningCost * count
                    round = count
        
        while extra > 0:
            if extra > 4:
                total += 4
                extra = extra-4
                count += 1
            else:
                total += extra
                extra = 0
                count += 1
            if total * boardingCost - runningCost * count > profit:
                    profit = total * boardingCost - runningCost * count
                    round = count
        if profit > 0:
            return round
        else:
            return -1
