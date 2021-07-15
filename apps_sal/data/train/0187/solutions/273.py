class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        a = []
        
        c = 0
        n = len(customers)
        i = 0
        while i < n or c > 0:
            if i < n:
                c += customers[i]
            b = 4 if c >= 4 else c
            p = b * boardingCost - runningCost
            a.append(p if len(a) == 0 else a[-1]+p)
            c -= b
            i += 1
        
        mIdx = 0
        for (i, v) in enumerate(a):
            if a[i] > a[mIdx]:
                mIdx = i
        if a[mIdx] <= 0:
            return -1
        else:
            return mIdx+1
