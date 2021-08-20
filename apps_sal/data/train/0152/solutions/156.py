class Solution:

    def maxDistance(self, A: List[int], m: int) -> int:
        A.sort()

        def valid(i):
            cnt = 1
            cur = A[0]
            for x in A[1:]:
                if x - cur >= i:
                    cnt += 1
                    cur = x
                if cnt >= m:
                    return True
            return False
        (l, r) = (1, A[-1])
        while l < r:
            mid = (l + r) // 2
            if valid(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1
