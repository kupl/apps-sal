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
            cost += boardingCost * grps[i] - runningCost
            if mex < cost:
                mex = max(mex, cost)
                ind = i + 1
        if mex < 0:
            return -1
        return ind
