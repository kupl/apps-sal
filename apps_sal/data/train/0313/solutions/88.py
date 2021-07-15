class Solution:
    def minDays(self, bloomDay: List[int], n: int, k: int) -> int:
        def ok(m, n):
            bloomed = [d <= m for d in bloomDay]
            c = i = j = 0
            while i < len(bloomed)-k+1:
                for _ in range(k):
                    if bloomed[j]:
                        j += 1
                    else:
                        i = j = j+1
                        break
                else:
                    i = j
                    c += 1
                    if c == n:
                        break
            else:
                return False
            return True
        
        
        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            m = (l+r) // 2
            if ok(m, n):
                r = m
            else:
                l = m+1
        return l if ok(l, n) else -1
