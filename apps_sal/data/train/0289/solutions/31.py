class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        acc = [0] + [*itertools.accumulate(A)]

        def getmaxfrom(i, x):
            return max(acc[j + x] - acc[j] for j in range(i, len(acc) - x))

        ans = 0
        s = 0
        i = 0
        for j in range(len(A) - M):
            s += A[j]
            if j - i == L:
                s -= A[i]
                i += 1
            ans = max(ans, s + getmaxfrom(j + 1, M))

        s = 0
        i = 0
        for j in range(len(A) - L):
            s += A[j]
            if j - i == M:
                s -= A[i]
                i += 1
            ans = max(ans, s + getmaxfrom(j + 1, L))
        return ans
