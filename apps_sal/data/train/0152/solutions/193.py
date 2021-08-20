class Solution:

    def maxDistance(self, A: List[int], m: int) -> int:
        n = len(A)
        A.sort()

        def balls(d):
            (count, cur) = (1, A[0])
            for i in range(1, len(A)):
                if A[i] - cur >= d:
                    count += 1
                    cur = A[i]
            return count
        (l, r) = (1, A[-1] - A[0])
        while l < r:
            mid = (l + r + 1) // 2
            if balls(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l
