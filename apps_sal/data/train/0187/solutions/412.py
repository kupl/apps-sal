class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        while len(customers) > 0 and customers[-1] == 0:
            customers.pop()
        wait = 0
        ans = 0
        max_ans = 0
        count = 0
        best_count = -1
        for i in range(len(customers)):
            wait += customers[i]
            ans -= runningCost
            ans += min(4, wait) * boardingCost
            wait -= min(4, wait)
            count += 1
            if ans > max_ans:
                max_ans = ans
                best_count = count
        while wait > 0:
            ans -= runningCost
            ans += min(4, wait) * boardingCost
            wait -= min(4, wait)
            count += 1
            if ans > max_ans:
                max_ans = ans
                best_count = count
        return best_count
