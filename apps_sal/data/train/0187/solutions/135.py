class Solution:
    def minOperationsMaxProfit(self, A, BC, RC):
        ans = profit = t = 0
        maxprofit = 0
        wait = i = 0
        n = len(A)
        while wait or i < n:
            if i < n:
                wait += A[i]
                i += 1
            t += 1
            y = min(4, wait)
            wait -= y
            profit += y * BC
            profit -= RC
            if profit > maxprofit:
                maxprofit = profit
                ans = t

        if maxprofit <= 0:
            return -1
        else:
            return ans
