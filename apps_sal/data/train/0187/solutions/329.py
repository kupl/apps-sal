from collections import deque


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = deque([])
        customers = deque(customers)
        waiting.append(customers.popleft())
        time = 1
        maxx = 0
        cost = 0
        ans = 0
        found = False
        total = 0
        while waiting or customers:
            curr = waiting.popleft()
            if curr > 4:
                curr -= 4
                total += 4
                waiting.appendleft(curr)
                cost = total * boardingCost - (time * runningCost)
            else:
                temp = curr
                while waiting and temp + waiting[0] <= 4:
                    temp += waiting.popleft()
                if temp < 4:
                    if waiting:
                        extra = 4 - temp
                        waiting[0] -= extra
                        temp = 4
                total += temp
                cost = total * boardingCost - (time * runningCost)
            if cost > maxx:
                maxx = cost
                found = True
                ans = time
            time += 1
            if customers:
                waiting.append(customers.popleft())
        return ans if found else -1
