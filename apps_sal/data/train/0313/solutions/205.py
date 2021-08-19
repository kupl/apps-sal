class Solution:

    def minDays(self, A: List[int], m: int, k: int) -> int:
        if len(A) < m * k:
            return -1

        def canSplit(T):
            count = 0
            cur = 0
            i = 0
            for x in A:
                cur = max(cur, x)
                i += 1
                if cur > T:
                    cur = 0
                    i = 0
                elif i == k:
                    cur = 0
                    i = 0
                    count += 1
            return count >= m
        l = min(A)
        r = max(A)
        while l < r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                r = mid
            else:
                l = mid + 1
        return l
