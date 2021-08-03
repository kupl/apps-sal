class Solution:
    def minDays(self, A: List[int], m: int, k: int) -> int:
        if len(A) < m * k:
            return -1

        def count(v):
            ret, ct = 0, 0
            for a in A:
                if a <= v:
                    ct += 1
                else:
                    ct = 0
                if ct == k:
                    ret += 1
                    ct = 0
            return ret

        left, right = min(A), max(A)
        while left < right:
            mid = (left + right) // 2
            if count(mid) < m:
                left = mid + 1
            else:
                right = mid
        return left
