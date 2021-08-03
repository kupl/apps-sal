class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        N = len(position)
        A = position
        A.sort()

        lo, hi = 1, A[-1] - A[0]
        while lo <= hi:
            mid = (lo + hi + 1) // 2

            prev = A[0]
            left = m - 1
            for i in range(1, N):
                if A[i] - prev >= mid:
                    prev = A[i]
                    left -= 1
                    if left == 0:
                        break

            if left == 0:
                answer = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return answer
