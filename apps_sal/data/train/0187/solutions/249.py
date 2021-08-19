class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waitingCustomer = 0
        numRotate = 0
        totalIncome = 0

        maxIncome = totalIncome
        rotateTime = -1

        while(waitingCustomer > 0 or numRotate < len(customers)):
            if(numRotate < len(customers)):
                waitingCustomer += customers[numRotate]

            # number of customer onboard this round
            numOnboard = min(4, waitingCustomer)
            waitingCustomer -= numOnboard

            # calculate income
            totalIncome += numOnboard * boardingCost - runningCost

            # rotate the wheel
            numRotate += 1

            if(totalIncome > maxIncome):
                maxIncome = totalIncome
                rotateTime = numRotate

        return rotateTime
