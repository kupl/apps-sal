class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        profit, Customers, waiting, rotation, R = 0, 0, 0, -1, 0
        size = len(customers)
        for i in range(size):
            waiting += customers[i]
            R += 1
            if waiting > 4:
                Customers += 4
                waiting -= 4
            else:
                Customers += waiting
                waiting = 0
            price = Customers * boardingCost - R * runningCost
            if price > profit:
                profit = price
                rotation = R
        while waiting:
            R += 1
            if waiting > 4:
                Customers += 4
                waiting -= 4
            else:
                Customers += waiting
                waiting = 0
            price = Customers * boardingCost - R * runningCost
            if price > profit:
                profit = price
                rotation = R

        return rotation
