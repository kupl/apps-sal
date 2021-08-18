class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        profit = 0
        waiting = 0
        rotations = 0
        onboard = 0
        gondola_customers = deque([])
        total = 0
        maxprofit = 0
        max_rotation = -1
        for arrival in customers:
            if gondola_customers:
                coming_down = gondola_customers.popleft()
                onboard -= coming_down

            total = arrival
            if waiting > 0:
                total = waiting + arrival

            if total <= 4:
                profit += ((total * boardingCost) - runningCost)
                onboard += total
                gondola_customers.append(total)
                waiting = max(0, waiting - total)
            else:
                profit += ((4 * boardingCost) - runningCost)
                onboard += 4
                gondola_customers.append(4)
                waiting += (arrival - 4)

            rotations += 1
            if profit > maxprofit:
                maxprofit = profit
                max_rotation = rotations
        print((maxprofit, max_rotation, waiting))
        profit += ((waiting // 4) * ((4 * boardingCost) - runningCost))
        rotations += (waiting // 4)
        if profit > maxprofit:
            maxprofit = profit
            max_rotation = rotations
        print((maxprofit, max_rotation, waiting % 4))

        profit += (((waiting % 4) * boardingCost) - runningCost)
        rotations += ((waiting % 4) > 0)
        if profit > maxprofit:
            maxprofit = profit
            max_rotation = rotations
        print((maxprofit, max_rotation))

        return max_rotation if maxprofit > 0 else -1
