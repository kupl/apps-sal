class Solution:

    def minScoreTriangulation(self, A: List[int]) -> int:

        def get(l, r):
            if r - l == 1:
                return 0
            if (l, r) in d:
                return d[l, r]
            res = min([A[l] * A[r] * A[i] + get(l, i) + get(i, r) for i in range(l + 1, r)])
            d[l, r] = res
            return res
        d = {}
        return get(0, len(A) - 1)
