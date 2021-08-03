class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:

        bound = r = 0
        gmax = lmax = A[0]
        while r < len(A):
            if A[r] >= gmax:
                lmax = max(lmax, A[r])
                r += 1
            else:
                bound = r
                gmax = max(gmax, lmax)
                r += 1

        return bound + 1
