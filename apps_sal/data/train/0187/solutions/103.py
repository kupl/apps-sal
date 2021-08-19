class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        arrive = 0
        board = 0
        wait2 = 0
        total = 0
        profit = 0
        length = len(customers)
        maxprofit = 0
        max_num = -1
        num = 0
        count = 0
        for i in range(length):
            arrive = customers[i]
            wait2 += arrive
            num += 1
            if wait2 >= 4:
                board = 4
                wait2 = wait2 - 4
            else:
                board = wait2
                wait2 = 0
            count += board
            profit = count * boardingCost - num * runningCost
            if profit > maxprofit:
                maxprofit = profit
                max_num = num
        while wait2 > 0:
            num += 1
            if wait2 >= 4:
                board = 4
                wait2 = wait2 - 4
            else:
                board = wait2
                wait2 = 0
            count += board
            profit = count * boardingCost - num * runningCost
            if profit > maxprofit:
                maxprofit = profit
                max_num = num
        return max_num
