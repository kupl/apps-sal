class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        sol = 1
        l_d = [{} for _ in range(n)]
        for j in range(1, n):
            dj = l_d[j]
            for i in range(j):
                diff = A[j] - A[i]
                di = l_d[i]
                dj[diff] = max(dj.get(diff, 2), di.get(diff, 1) + 1)
                sol = max(sol, dj[diff])

        return sol
