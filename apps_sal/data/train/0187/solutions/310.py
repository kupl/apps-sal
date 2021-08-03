class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if len(customers) == 0:
            return 0

        self.res = float('-inf')
        self.rotation = 0
        cuswaiting = 0
        profit = 0
        rotation = 0
        attendcus = 0

        while cuswaiting != 0 or rotation < len(customers):
            if rotation < len(customers):
                cuswaiting += customers[rotation]
            rotation += 1

            if cuswaiting >= 4:
                attendcus += 4
                profit = attendcus * boardingCost - rotation * runningCost
                cuswaiting -= 4
            else:
                attendcus += cuswaiting
                profit = attendcus * boardingCost - rotation * runningCost
                cuswaiting = 0

            #print(profit, rotation)
            if self.res < profit:
                self.res = profit
                self.rotation = rotation

        if self.res < 0:
            return -1
        else:
            return self.rotation
