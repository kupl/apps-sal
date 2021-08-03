class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:

        def helper(i, j):
            key = (i, j)
            if key in d:
                return d[key]
            if j - i < 2:
                return 0
            ans = float('inf')

            for k in range(i + 1, j):

                lans = helper(i, k)
                rans = helper(k, j)
                ans = min(ans, lans + rans + A[i] * A[j] * A[k])
            d[key] = ans
            return d[key]
        d = dict()
        return helper(0, len(A) - 1)
