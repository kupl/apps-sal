class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        customers.reverse()
        wait = 0
        board = 0
        turn = 0
        ans = -1
        score = 0
        while wait or customers:
            turn += 1
            if customers:
                wait += customers.pop()
            if wait >= 4:
                board += 4
                wait -= 4
            else:
                board += wait
                wait = 0
            if score < board * boardingCost - turn * runningCost:
                ans = turn
                score = board * boardingCost - turn * runningCost
        return ans
