class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost > 4 * boardingCost:
            return -1
        profit = 0
        board = 0
        wait = 0
        ans = 0
        for i in range(len(customers)):
            if customers[i] > 4:
                wait += customers[i] - 4
                board += 4
                p = board * boardingCost - (i + 1) * runningCost
                if p > profit:
                    profit = p
                    ans = i + 1
            else:
                add = min(wait, 4 - customers[i])
                wait -= add
                board += add + customers[i]
                p = board * boardingCost - (i + 1) * runningCost
                if p > profit:
                    profit = p
                    ans = i + 1

        i = len(customers)
        while wait != 0:
            add = min(wait, 4)
            board += add
            wait -= add
            p = board * boardingCost - (i + 1) * runningCost
            if p > profit:
                profit = p
                ans = i + 1
            i += 1

        return ans
