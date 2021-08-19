class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        if len(A) == 1 or len(A) == 2:
            return len(A)
        D = [dict() for _ in range(len(A))]
        ans = 0
        for (i, a) in enumerate(A[1:], 1):
            for j in range(i):
                if a - A[j] not in D[j]:
                    D[i][a - A[j]] = 2
                else:
                    D[i][a - A[j]] = D[j][a - A[j]] + 1
            ans = max(ans, max(D[i].values()))
        return ans
