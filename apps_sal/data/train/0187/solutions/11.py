class Solution:
    def minOperationsMaxProfit(self, comes, bC, rC):
        totalProfit = 0
        curRotate = 0
        maxProfit = -1
        maxRotate = 0
        
        waiting = 0
        for come in comes:
            waiting += come
            if waiting < 4:
                totalProfit += waiting * bC
                waiting = 0
            else:
                totalProfit += 4 * bC
                waiting -= 4
            totalProfit -= rC
            curRotate += 1
            
            if totalProfit > maxProfit:
                maxProfit = totalProfit
                maxRotate = curRotate
        
        while waiting:
            if waiting < 4:
                totalProfit += waiting * bC
                waiting = 0
            else:
                totalProfit += 4 * bC
                waiting -= 4
            totalProfit -= rC
            curRotate += 1
            
            if totalProfit > maxProfit:
                maxProfit = totalProfit
                maxRotate = curRotate
        
        return maxRotate if maxProfit > 0 else -1

