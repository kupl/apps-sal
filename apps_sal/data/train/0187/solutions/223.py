class Solution:
    def minOperationsMaxProfit(self, arr: List[int], boardingCost: int, runningCost: int) -> int:
        grps = []
        n = len(arr)
        rem = 0

        for i in range(n):
            avail = arr[i] + rem
            if avail >= 4:
                avail -= 4
                grps.append(4)
                rem = avail
            else:
                rem = 0
                grps.append(avail)

        while rem > 0:
            if rem >= 4:
                rem -= 4
                grps.append(4)
            else:
                grps.append(rem)
                rem = 0

        mex = -10**10
        cost = 0
        ind = 0
        for i in range(len(grps)):
            # calculate net cost till now
            cost += boardingCost * grps[i] - runningCost
            # upadte max profit and rotation number
            if mex < cost:
                mex = max(mex, cost)
                ind = i + 1
        # max profit< 0
        if mex < 0:
            return -1
        # return rotation number
        return ind

        # idx = 0
        # profit = 0
        # max_idx = -1
        # max_profit = 0
        # n_cus = 0
        # for cus in customers:
        #     idx += 1
        #     profit += min(4, cus) * boardingCost - runningCost
        #     n_cus += max(cus-4, 0)
        #     if profit > max_profit:
        #         max_idx = idx
        #         max_profit = profit
        # if n_cus >= 4:
        #     if 4*boardingCost <= runningCost:
        #         return max_idx
        #     else:
        #         profit += (4*boardingCost - runningCost) * (n_cus // 4)
        #         idx += n_cus // 4
        #         n_cus %= 4
        #         if profit > max_profit:
        #             max_idx = idx
        #             max_profit = profit
        # idx += 1
        # profit += n_cus * boardingCost - runningCost
        # if profit > max_profit:
        #     max_idx = idx
        # return max_idx
