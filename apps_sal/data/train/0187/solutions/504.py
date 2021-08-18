class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        if boardingCost * 4 < runningCost:
            return -1

        currVisitor = 0
        currGondolas = 0
        currProfit = 0
        currRotation = 0
        maxProf = 0
        maxProf_rot = -1
        gondolas = collections.deque()
        totPeople = 0
        for customer in customers:
            currRotation += 1
            currVisitor += customer
            if currGondolas < 4:
                gondolas.append(min(currVisitor, 4))
                currGondolas = len(gondolas)
            else:
                gondolas.pop()
                gondolas.append(min(currVisitor, 4))
            totPeople += min(currVisitor, 4)
            currVisitor -= min(currVisitor, 4)
            currProfit = boardingCost * totPeople - currRotation * runningCost

            if currProfit > maxProf:
                maxProf = currProfit
                maxProf_rot = currRotation

        while currVisitor > 0:
            currRotation += 1
            if currGondolas < 4:
                gondolas.append(min(currVisitor, 4))
                currGondolas = len(gondolas)
            else:
                gondolas.pop()
                gondolas.append(min(currVisitor, 4))
            totPeople += min(currVisitor, 4)
            currVisitor -= min(currVisitor, 4)

            currProfit = boardingCost * totPeople - currRotation * runningCost

            if currProfit > maxProf:
                maxProf = currProfit
                maxProf_rot = currRotation

        return maxProf_rot


'''
1. 10 customers arrive, 4 board and 6 wait for the next gondola, the wheel rotates. Current profit is 4 * $6 - 1 * $4 = $20.
2. 9 customers arrive, 4 board and 11 wait (2 originally waiting, 9 newly waiting), the wheel rotates. Current profit is 8 * $6 - 2 * $4 = $40.
3. The final 6 customers arrive, 4 board and 13 wait, the wheel rotates. Current profit is 12 * $6 - 3 * $4 = $60.
4. 4 board and 9 wait, the wheel rotates. Current profit is 16 * $6 - 4 * $4 = $80.
5. 4 board and 5 wait, the wheel rotates. Current profit is 20 * $6 - 5 * $4 = $100.
6. 4 board and 1 waits, the wheel rotates. Current profit is 24 * $6 - 6 * $4 = $120.
7. 1 boards, the wheel rotates. Current profit is 25 * $6 - 7 * $4 = $122.
The highest profit was $122 after rotating the wheel 7 times.
 '''
