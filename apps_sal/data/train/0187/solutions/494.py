class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ln = len(customers)
        folks = 0
        rotate = 0
        profit = 0
        mxProfit = -1
        mxProfitRotate = 0
        while rotate < ln or folks > 0:
            folks += customers[rotate] if rotate < ln else 0
            profit += min(folks, 4)*boardingCost - runningCost
            folks = max(folks - 4, 0)
            if profit > mxProfit:
                mxProfit = profit
                mxProfitRotate = rotate + 1
            rotate += 1
            
            
        return -1 if mxProfit < 0 else mxProfitRotate
