class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo, hi = max(weights), sum(weights)   
        while lo < hi:
            mid = (lo + hi) // 2
            tot, res = 0, 1
            for wt in weights:
                if tot + wt > mid:
                    res += 1
                    tot = wt
                    # print(\"res\", res)
                    
                else:
                    tot += wt
            if res <= D:
                hi = mid
                # print(\"hi\",hi)
            else:
                lo = mid+1
                # print(\"lo\",lo)
        return lo
