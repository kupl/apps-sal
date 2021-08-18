class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        i = 0
        g = [4, 4, 4, 4]

        profit = 0
        max_profit = 0
        customers = customers[::-1]
        rotates = 0
        best = -1
        while customers:
            g[i] = 4
            c = customers.pop()
            if c - g[i] > 0:
                c -= g[i]
                profit += g[i] * boardingCost
                g[i] = 0
                if customers:
                    customers[-1] = customers[-1] + c
                else:
                    customers = [c]
            else:
                g[i] -= c
                profit += c * boardingCost
            profit -= runningCost
            rotates += 1
            if profit > max_profit:
                best = rotates
                max_profit = profit
            i += 1
            i %= 4
        return best
