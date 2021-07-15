class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1
        s, r, maxr, maxn = 0, 0, 0, -1
        for i, c in enumerate(customers):
            s += c
            b = min(s, 4)
            r += b * boardingCost - runningCost
            s -= b
            if r > maxr:
                maxr, maxn = r, i+1
        r += 4 * (s // 4) * boardingCost - (s // 4) * runningCost
        if r > maxr:
            maxr, maxn = r, len(customers) + (s // 4)
        if s % 4 > 0:
            r += (s % 4) * boardingCost - runningCost
            if r > maxr:
                maxr, maxn = r, len(customers) + (s // 4) + 1
        return maxn
