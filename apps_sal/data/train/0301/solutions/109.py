class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (nA, nB) = (len(A), len(B))
        if nA == 0 or nB == 0:
            return 0
        cache = {}

        def process(iA, iB):
            if iA < 0 or iB < 0:
                return 0
            if not (iA, iB) in cache:
                ans = 0
                if A[iA] == B[iB]:
                    ans = 1 + process(iA - 1, iB - 1)
                else:
                    ans = max(process(iA - 1, iB), process(iA, iB - 1))
                cache[iA, iB] = ans
            return cache[iA, iB]
        return process(nA - 1, nB - 1)
