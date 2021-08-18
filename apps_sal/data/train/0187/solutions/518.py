class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        r = 1
        wait = 0
        cost = 0
        cround = []
        for c in customers:
            wait += c
            if wait >= 4:
                wait -= 4
                cost += boardingCost * 4 - runningCost
                cround.append([cost, r])
            elif wait > 0:
                cost += boardingCost * wait - runningCost
                wait -= wait
                cround.append([cost, r])
            r += 1

        while wait >= 4:
            wait -= 4
            cost += boardingCost * 4 - runningCost
            cround.append([cost, r])
            r += 1

        if wait > 0:
            cost += boardingCost * wait - runningCost
            cround.append([cost, r])
            wait -= wait
            r += 1

        ans = max(cround, key=lambda x: x[0])
        if ans[0] > 0:
            return ans[1]
        else:
            return -1
