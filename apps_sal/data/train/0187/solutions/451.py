class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        curr = 0 
        waiting = 0
        ans = 0
        i = 0
        mI = -1
        m = 0
        while i < len(customers) or waiting:
            # print(i, curr, waiting, ans)
            waiting += customers[i] if i < len(customers) else 0
            curr += min(waiting, 4)
            waiting -= min(waiting, 4)
            ans = (curr * boardingCost) - ((i+1) * runningCost)

            i += 1
            if ans > m:
                mI = i
                # print(ans)
                m = ans
        # print(i, curr)
        return mI

