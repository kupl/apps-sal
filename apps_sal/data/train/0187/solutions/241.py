class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        c = 0
        w = customers[c]
        c = c + 1
        l = []
        t = 0
        i = 0
        while w != 0 or c < n:
            i = i + 1
            if w >= 4:
                w = w - 4
                t = t + 4
            else:
                t = t + w
                w = 0
            if c < n:
                w = w + customers[c]
                c = c + 1
            l.append(t * boardingCost - i * runningCost)
        m = max(l)
        if m < 0:
            return -1
        else:
            return l.index(m) + 1
