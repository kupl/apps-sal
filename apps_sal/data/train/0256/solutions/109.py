class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lenth = len(piles)
        s = (min(piles) - 1) * lenth // H + 1
        m = (max(piles) - 1) * lenth // H + 1
        if int(m) < m:
            m = int(m) + 1
        if s == m:
            return s
        while s < m:
            mid = (s + m) // 2
            count = sum([(i - 1) // mid + 1 for i in piles])
            if count > H:
                s = mid + 1
            else:
                m = mid
        return s
