class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:
            return -1
        wheelCount = 0
        numOfCustomers = 0
        for customer in customers:
            numOfCustomers += customer
            boardingUsers = min(4, numOfCustomers)
            wheelCount += 1
            if boardingUsers * boardingCost > runningCost:
                numOfCustomers -= boardingUsers
        while numOfCustomers:
            boardingUsers = min(4, numOfCustomers)
            if boardingUsers * boardingCost > runningCost:
                wheelCount += 1
            numOfCustomers -= boardingUsers
        return wheelCount
