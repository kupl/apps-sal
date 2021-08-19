class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wheel = [0, 0, 0, 0]
        profit = 0
        tracker = [-1]
        line = 0

        def rotate(wheel, profit, boardingCost, runningCost, tracker):
            profit += boardingCost * wheel[0] - runningCost
            tracker.append(profit)
            wheel = [0, wheel[0], wheel[1], wheel[2]]
            return (wheel, profit, tracker)
        i = 0
        while i < len(customers) or line > 0:
            if i < len(customers):
                line += customers[i]
            if line <= 4:
                wheel[0] = line
                line = 0
            else:
                wheel[0] = 4
                line -= 4
            (wheel, profit, tracker) = rotate(wheel, profit, boardingCost, runningCost, tracker)
            i += 1
        maxp = -1
        val = -1
        for i in range(len(tracker)):
            if tracker[i] > maxp:
                maxp = tracker[i]
                val = i
        if maxp > 0:
            return val
        else:
            return -1
