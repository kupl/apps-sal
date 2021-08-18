class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        amt = 0
        max = 0
        boarded = 0
        waiting = 0
        cur = 0

        rot = 0
        min = 0

        for i in range(0, len(customers)):

            rot = rot + 1

            waiting = waiting + customers[i]

            if (waiting >= 4):
                boarded = boarded + 4
                waiting = waiting - 4
                cur = cur + 4
            else:
                boarded = boarded + waiting
                cur = cur + waiting
                waiting = 0

            amt = boarded * boardingCost - rot * runningCost

            if (max < amt):
                max = amt
                min = rot

        while (waiting > 0):

            rot = rot + 1

            if (waiting >= 4):
                boarded = boarded + 4
                cur = cur + 4
                waiting = waiting - 4
            else:
                boarded = boarded + waiting
                cur = cur + waiting
                waiting = 0

            amt = boarded * boardingCost - rot * runningCost

            if (max < amt):
                max = amt
                min = rot

        if (max == 0):
            return -1
        else:
            return min
