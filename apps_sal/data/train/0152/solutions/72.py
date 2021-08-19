class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        N = len(position)
        A = sorted(position)
        max_gap = A[-1] - A[0]
        min_gap = min((A[i] - A[i - 1] for i in range(1, N)))
        if m == 2:
            return max_gap
        if m == N:
            return min_gap

        def check(min_dist):
            prev = A[0]
            left = m - 1
            for i in range(1, N):
                if A[i] - prev >= mid:
                    prev = A[i]
                    left -= 1
                    if left == 0:
                        return True
            return False
        (lo, hi) = (min_gap, max_gap)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            c = check(mid)
            if c:
                lo = mid
            else:
                hi = mid - 1
        return lo
