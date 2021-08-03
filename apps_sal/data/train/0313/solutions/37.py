class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        mi, ma = min(bloomDay), max(bloomDay)
        while(mi < ma):
            mid = (mi + ma) // 2
            curr = 0
            adj = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] > mid:
                    adj = 0
                else:
                    adj += 1
                    if adj == k:
                        adj = 0
                        curr += 1
                if curr >= m:
                    break
            if curr < m:
                mi = mid + 1
            else:
                ma = mid
        return (mi)
