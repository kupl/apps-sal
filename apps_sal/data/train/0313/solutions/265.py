class Solution:
    def minDays(self, bloomDay: List[int], M: int, K: int) -> int:
        if len(bloomDay) < M * K : return -1
        def condition(day) -> bool:
            m, k = 0, 0
            for bd in bloomDay:
                if bd <= day : k += 1
                else : k = 0
                if k >= K : 
                    m += 1
                    k = 0
                if m >= M : return True
            return False

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left        
