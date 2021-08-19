class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        maxp = 0
        curr = 0
        c = 0
        track = 0
        for i in range(len(customers)):
            track += customers[i]
            curr += min(4, track) * boardingCost - runningCost
            track -= min(4, track)
            c += 1
            if curr > maxp:
                maxp = curr
                ans = c
        if track >= 4:
            curr += (track - track % 4) * boardingCost - track // 4 * runningCost
            c += track // 4
            if curr > maxp:
                maxp = curr
                ans = c
        curr += track % 4 * boardingCost - runningCost
        c += 1
        if curr > maxp:
            maxp = curr
            ans = c
        return ans
