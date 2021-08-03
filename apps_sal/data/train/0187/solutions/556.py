class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        avail, cur, high, high_idx = 0, 0, 0, -1
        for i, c in enumerate(customers):
            avail += c
            if avail > 4:
                cur += 4 * boardingCost - runningCost
                avail -= 4
            else:
                cur += avail * boardingCost - runningCost
                avail = 0
            if cur > high:
                high, high_idx = cur, i + 1

        if 4 * boardingCost - runningCost > 0:
            i += avail // 4
            cur += (4 * boardingCost - runningCost) * (avail // 4)
            avail = avail % 4
            high, high_idx = cur, i + 1

            cur += avail * boardingCost - runningCost
            avail = 0
            if cur > high:
                high, high_idx = cur, high_idx + 1

        return high_idx
