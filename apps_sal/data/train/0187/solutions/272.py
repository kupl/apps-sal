class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        waitingList = 0
        maxProfit = 0
        rotations = 0
        maxR = 0
        counter = 0
        totalCustomer = 0
        
        maxRotations = -1
        maxProfit = profit = waitingList = 0
        for index, val in enumerate(customers): 
            waitingList += val # more people waiting in line 
            ##People boarded
            peopleBoarded = min(4, waitingList)
            waitingList -= peopleBoarded # boarding 
            profit += peopleBoarded * boardingCost - runningCost 
            if maxProfit < profit: maxRotations, maxProfit = index+1, profit
        waitingloop, waitingrem = divmod(waitingList, 4)
        if 4*boardingCost > runningCost: maxRotations += waitingloop
        if waitingrem*boardingCost > runningCost: maxRotations += 1
        return maxRotations 
