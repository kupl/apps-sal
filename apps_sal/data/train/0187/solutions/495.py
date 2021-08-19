class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        gondola = collections.deque([0, 0, 0, 0])
        backlog = customers[0]
        customers_index = 1
        profit = 0
        rotations = 0
        max_profit, min_rotations = 0, 0

        while backlog or customers_index < len(customers):
            gondola.popleft()

            gondola.append(min(backlog, 4))
            profit = profit + (min(backlog, 4) * boardingCost) - runningCost
            rotations += 1
            backlog = max(backlog - 4, 0)

            if profit > max_profit:
                max_profit = profit
                min_rotations = rotations

            # if cost > 0 and new_cost <= cost:
            #     break
            # cost = new_cost

            if customers_index < len(customers):
                backlog += customers[customers_index]
                customers_index += 1

        if profit < 0:
            return -1
        else:
            return min_rotations
