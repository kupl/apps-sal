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
        for idx, arrival in enumerate(customers):
            # if onboard == 0 and waiting == 0 and arrival == 0:
            # continue

            if gondola_customers and gondola_customers[0][1] == idx:
                coming_down = gondola_customers.popleft()[0]
                onboard -= coming_down

            total = arrival
            if waiting > 0:
                total = waiting + arrival

            board = min(total, 4)
            profit += ((board * boardingCost) - runningCost)
            onboard += board
            gondola_customers.append([board, idx + 4])
            waiting += (arrival - board)

            rotations += 1
            if profit > maxprofit:
                maxprofit = profit
                max_rotation = rotations

        profit += ((waiting // 4) * ((4 * boardingCost) - runningCost))
        rotations += (waiting // 4)
        if profit > maxprofit:
            maxprofit = profit
            max_rotation = rotations

        profit += (((waiting % 4) * boardingCost) - runningCost)
        rotations += ((waiting % 4) > 0)
        if profit > maxprofit:
            maxprofit = profit
            max_rotation = rotations

        return max_rotation if maxprofit > 0 else -1
