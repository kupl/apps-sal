class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        total = 0
        l = len(customers)
        i = 0
        board = 0
        rotation = 0
        maxsum = 0
        maxrot = -1
        while total > 0 or i < l :
            if i < l :
                total += customers[i]
                i += 1
            if total > 4:
                board += 4
                total -= 4
            else:
                board += total
                total = 0
            rotation += 1
            temp = board*boardingCost - rotation*runningCost
            if temp > maxsum:
                maxrot = rotation
                maxsum = temp

        return maxrot

