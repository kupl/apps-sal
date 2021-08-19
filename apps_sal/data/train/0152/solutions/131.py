class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def ispossible(A, force, n):
            n -= 1
            last = A[0]
            for i in range(1, len(A)):
                if n > 0:
                    if A[i] - last >= force:
                        n -= 1
                        last = A[i]
                else:
                    break
            if n == 0:
                return True
            return False
        A = position
        A.sort()
        l = 1
        r = A[-1]
        ans = 1
        while r >= l:
            mid = (r + l) // 2
            if ispossible(A, mid, m):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
