class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 1; r = int(1e9)
        def check(days, k):
            made = 0
            soFar = 0
            for i in range(len(bloomDay)):
                if(bloomDay[i] > days):
                    soFar = 0
                else:
                    soFar += 1
                if(soFar == k):
                    soFar = 0
                    made += 1
            return made
        while(l < r):
            mid = l+((r-l)>>1)
            if(check(mid, k) >= m):
                r = mid
            else:
                l = mid+1
        if(check(l, k) >= m):
            return l
        return -1
