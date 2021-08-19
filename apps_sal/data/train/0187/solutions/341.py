class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        sm = 0
        cus = 0
        c = 0
        w = 0
        ret = 0
        mx = 0
        while True:
            if c < len(customers):
                cus += customers[c]
                c += 1
            board = min(4, cus)
            cus -= board
            sm += boardingCost * board - runningCost
            w += 1
            if mx < sm:
                ret = w
                mx = sm
            if 0 == min(4, cus) and c == len(customers):
                break
        return -1 if mx == 0 else ret
