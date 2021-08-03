class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if not bloomDay or m * k > len(bloomDay):
            return(-1)

        def feasible(days):
            bouquets, flower = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flower = 0
                else:
                    bouquets += (flower + 1) // k
                    flower = (flower + 1) % k
            return bouquets >= m
        l, r = 0, max(bloomDay)
        while(l < r):
            mid = l + (r - l) // 2
            if(feasible(mid)):
                r = mid
            else:
                l = mid + 1
        return l
