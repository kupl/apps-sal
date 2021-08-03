class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost:
            return -1
        result = sum(customers) // 4
        if (sum(customers) % 4) * boardingCost > runningCost:
            result += 1
        for customer in customers:
            if customer <= 1:
                result += 1
            else:
                break
        return result
