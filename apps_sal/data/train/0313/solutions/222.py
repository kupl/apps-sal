class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            flow = bouq = 0
            for bloom in bloomDay:
                if bloom > mid:
                    flow = 0
                else:
                    flow += 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: 
                        break
            if bouq == m:
                high = mid
            else:
                low = mid + 1
        return low
            

