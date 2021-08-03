class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = 0
        pres = customers[0]
        tc = 0
        hp = -1
        if(pres > 4):
            pres -= 4
            k = ans
            ans += 4 * boardingCost - runningCost
            tc += 1
            if(ans > k):
                hp = tc
        else:
            pres = 0
            k = ans
            ans += pres * boardingCost - runningCost
            tc += 1
            if(ans > k):
                hp = tc
        for i in range(1, len(customers)):
            pres += customers[i]
            if(pres > 4):
                pres -= 4
                k = ans
                ans += 4 * boardingCost - runningCost
                tc += 1
                if(ans > k):
                    hp = tc
            else:
                pres = 0
                k = ans
                ans += pres * boardingCost - runningCost
                tc += 1
                if(ans > k):
                    hp = tc
        while(pres > 4):
            pres -= 4
            k = ans
            ans += 4 * boardingCost - runningCost
            tc += 1
            if(ans > k):
                hp = tc
        if(pres != 0):
            k = ans
            ans += pres * boardingCost - runningCost
            tc += 1
            if(ans > k):
                hp = tc
        if(ans < 0):
            return -1
        return hp
