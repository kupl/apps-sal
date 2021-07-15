class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        best = 0, -1
        boarded = 0
        cur = rotations = 0
        for customer in customers:
            # print(cur, customer)
            cur += customer
            boarded += min(cur, 4)
            cur -= min(cur, 4)
            rotations += 1
            cur_revenue = boarded * boardingCost - rotations * runningCost
            if best[0] < cur_revenue:
                best = cur_revenue, rotations
            # print(rotations)
        while cur > 0:
            # print(cur)
            boarded += min(cur, 4)
            cur -= min(cur, 4)
            rotations += 1
            cur_revenue = boarded * boardingCost - rotations * runningCost
            if best[0] < cur_revenue:
                best = cur_revenue, rotations
        return best[1]
            
            
                
        # cur = boarded = rotations = 0
        # best = (0, 1)
        # for customer in customers:
        #     cur += customer
        #     if cur < 1:
        #         rotations += 1
        #         continue
        #     while cur > 0:
        #         rotations += 1
        #         boarded += 4
        #         cur = max(cur - 4, 0)
        #         best = max(best, (boarded * boardingCost - rotations * runningCost, -rotations))
        # print(cur, best)
        # # if cur > 0:
        # #     best = max(best, ((boarded + cur) * boardingCost - (rotations + 1) * runningCost, -(rotations+1)))
        # # print(cur, best)
        # return -best[1]

