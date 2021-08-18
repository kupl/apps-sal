class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        queue = deque(customers)
        profit = 0
        k = 0
        max_profit = 0
        max_k = 0
        while queue:
            num_people = queue.popleft()
            i = 1
            if num_people > 4:
                if queue:
                    queue[0] += num_people - 4
                else:
                    i = num_people // 4
                    queue.append(num_people - 4 * i)
                num_people = 4
            k += i
            profit += num_people * boardingCost * i
            profit -= runningCost * i
            if max_profit < profit:
                max_k = k
                max_profit = profit
        return max_k if max_profit > 0 else -1
