class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k: return -1
        l, r = 1, max(bloomDay)
        while l < r:
            p, curr, cnt = l + (r - l) // 2, 0, 0
            for x in bloomDay:
                curr = curr + 1 if x <= p else 0
                if curr == k:
                    cnt, curr = cnt+1, 0
                if cnt == m: break
            if cnt < m: l = p+1
            else: r = p
        return l
