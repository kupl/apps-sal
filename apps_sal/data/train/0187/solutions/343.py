class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        best_profit = float('-inf')
        best_rotations = -1
        rem = 0
        group = []
        for c in customers:
            avail = rem + c
            group.append(min(4, avail))
            rem = max(0, avail - 4)

        while rem:
            group.append(min(4, rem))
            rem = max(0, rem - 4)
        profit = cost = 0
        for i, g in enumerate(group):
            profit += g * boardingCost
            cost += runningCost
            if best_profit < profit - cost:
                best_profit = profit - cost
                best_rotations = i + 1

        return best_rotations if best_profit > 0 else -1
