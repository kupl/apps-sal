class Solution:

    def minDays(self, A: List[int], m: int, k: int) -> int:

        def valid(mid):
            cur = 0
            accu = 0
            for n in A:
                if n <= mid:
                    cur += 1
                    if cur == k:
                        accu += 1
                        cur = 0
                else:
                    cur = 0
            return accu >= m
        n = len(A)
        if m * k > n:
            return -1
        (l, r) = (min(A), max(A))
        while l < r:
            mid = (l + r) // 2
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return l
