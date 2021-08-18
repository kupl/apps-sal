class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = [0]
        left = 0
        maxMid = -1
        maxProfit = 0
        for i in range(len(customers)):
            toBeBoarded = left + customers[i]
            if toBeBoarded > 4:
                boarded = 4
                left = toBeBoarded - 4
            else:
                boarded = customers[i]
                left = 0
            newProfit = boardingCost * boarded - runningCost + profit[-1]
            profit.append(newProfit)
            if newProfit > maxProfit:
                maxProfit = newProfit
                maxMid = i
        if left == 0:
            return maxMid
        elif left < 4:
            lastProfit = boardingCost * left - runningCost + profit[-1]
            if maxProfit >= lastProfit:
                return maxMid + 1 if maxProfit > 0 else -1
            else:
                return len(customers) + 1 if lastProfit > 0 else -1
        else:
            potential = boardingCost * 4 - runningCost
            if potential > 0:
                rotations = left // 4
                lastRun = left % 4
                rotationEnd = profit[-1] + potential * rotations
                lastProfit = rotationEnd + lastRun * boardingCost - runningCost
                if maxProfit >= rotationEnd:
                    return maxMid + 1 if maxProfit > 0 else -1
                else:
                    if rotationEnd >= lastProfit:
                        return len(customers) + rotations if rotationEnd > 0 else -1
                    else:
                        return len(customers) + rotations + 1 if lastProfit > 0 else -1
            else:
                return maxMid + 1 if maxProfit > 0 else -1
