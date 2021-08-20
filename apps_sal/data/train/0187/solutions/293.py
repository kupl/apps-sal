class Solution:

    def minOperationsMaxProfit(self, A, BC, RC):
        ans = profit = t = 0
        maxprofit = 0
        wait = i = 0
        n = len(A)
        while wait > 0 or i < n:
            if i < n:
                wait += A[i]
                i += 1
            t += 1
            y = min(4, wait)
            if y > 0:
                wait -= y
                profit += y * BC
                profit -= RC
                if profit > maxprofit:
                    maxprofit = profit
                    ans = t
        return -1 if maxprofit <= 0 else ans
