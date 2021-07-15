class Solution:
    def maxDistance(self, A: List[int], m: int) -> int:
        A, n = sorted(A), len(A)
        left, right = 0, A[-1] - A[0]
        while left < right:
            mid = (right + left + 1) // 2
            ct, idx = 1, 0
            for i in range(1, n):
                if A[i] - A[idx] >= mid:
                    ct += 1
                    idx = i
            if ct < m:
                right = mid - 1
            else:
                left = mid
        return right
