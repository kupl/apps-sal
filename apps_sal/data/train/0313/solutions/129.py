class Solution:

    def minDays(self, days: List[int], m: int, k: int) -> int:
        n = len(days)
        if m * k > n:
            return -1
        (i, j) = (1, max(days))
        while i < j:
            day = (i + j) / 2
            bou = flow = 0
            for a in days:
                flow = 0 if a > day else flow + 1
                if flow >= k:
                    flow = 0
                    bou += 1
                    if bou == m:
                        break
            if bou == m:
                j = day
            else:
                i = day + 1
        return int(i)
