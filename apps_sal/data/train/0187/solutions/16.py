import math


class Solution:

    def minOperationsMaxProfit(self, cust: List[int], bc: int, rc: int) -> int:
        wait = 0
        count = 0
        profit = 0
        mxp = 0
        mxc = 0
        for i in range(len(cust)):
            count += 1
            temp = wait + cust[i]
            if temp > 4:
                wait = temp - 4
                profit += 4 * bc - rc
            else:
                profit += temp * bc - rc
                wait = 0
            if profit > mxp:
                mxp = profit
                mxc = count
        cur = math.ceil(wait / 4)
        if cur == 0:
            if mxp > 0:
                return mxc
            else:
                return -1
        else:
            while wait > 0:
                count += 1
                if wait <= 4:
                    profit += wait * bc - rc
                    if profit > mxp:
                        mxp = profit
                        mxc = count
                    break
                else:
                    profit += 4 * bc - rc
                    if profit > mxp:
                        mxp = profit
                        mxc = count
                    wait -= 4
            if mxp > 0:
                return mxc
            else:
                return -1
