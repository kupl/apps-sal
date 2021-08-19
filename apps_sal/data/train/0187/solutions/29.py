class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ccnt = 0
        output = []
        prof = 4 * boardingCost - runningCost
        for i in customers:
            ccnt += i
            if ccnt < 4:
                pro = ccnt * boardingCost - runningCost
                ccnt = 0
            else:
                pro = prof
                ccnt -= 4
            output.append(pro)
        while ccnt > 4:
            output.append(prof)
            ccnt -= 4
        output.append(ccnt * boardingCost - runningCost)
        maxv = totp = 0
        res = -1
        for (n, i) in enumerate(output):
            totp += i
            if totp > maxv:
                maxv = totp
                res = n + 1
        return res
