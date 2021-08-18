class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        maxCap = sum(weights)
        minCap = max(weights)
        ans = maxCap

        lo = minCap
        hi = maxCap

        while lo <= hi:
            mi = lo + (hi - lo) // 2
            daysLeft = D
            dailyCap = mi
            i = 0
            while i < len(weights) and daysLeft:
                wei = weights[i]
                if wei > dailyCap:
                    daysLeft -= 1
                    dailyCap = mi
                elif wei == dailyCap:
                    daysLeft -= 1
                    dailyCap = mi
                    i += 1
                else:
                    dailyCap -= wei
                    i += 1
            if i == len(weights):
                ans = min(ans, mi)
                hi = mi - 1
            else:
                lo = mi + 1
        return ans
