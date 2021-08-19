class Solution:

    def minOperationsMaxProfit(self, cust: List[int], board: int, run: int) -> int:
        wait = 0
        tot = 0
        profit = 0
        move = 1
        ans = 0
        maxi = 0
        for i in range(len(cust)):
            tot += min(4, cust[i] + wait)
            wait = max(0, cust[i] + wait - 4)
            profit = tot * board - move * run
            if profit > maxi:
                maxi = profit
                ans = move
            move += 1
        while wait > 0:
            tot += min(4, wait)
            wait -= 4
            profit = tot * board - move * run
            if profit > maxi:
                maxi = profit
                ans = move
            move += 1
        if maxi > 0:
            return ans
        return -1
