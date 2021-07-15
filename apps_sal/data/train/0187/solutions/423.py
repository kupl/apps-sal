class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost < runningCost:
            return -1
        curr_profit = max_profit = 0
        ans = 0
        running_round = 0
        queue = collections.deque([])
        max_queue = 0
        for customer in customers:
            if not queue and sum(queue) + customer < 4:
                queue.append(customer)
                continue
            if queue and queue[-1] < 4:
                index = len(queue) - 1
                while index >= 0:
                    if queue[index] == 4:
                        fill = min(4 - queue[-1], customer)
                        queue[-1] += fill
                        customer -= fill
                        break
                    index -= 1
            while customer >= 4:
                queue.append(4)
                customer -= 4
            if customer > 0:
                queue.append(customer)
        while queue:
            running_round += 1
            curr = queue.popleft()
            curr_profit += (curr * boardingCost - runningCost)
            if curr_profit > max_profit:
                ans = running_round
            max_profit = max(curr_profit, max_profit)
        return ans
