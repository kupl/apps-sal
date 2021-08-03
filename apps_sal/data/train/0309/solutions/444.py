class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        lim = len(A)

        d = dict()
        ans = []
        for i in range(0, lim):
            d[i] = dict()
            ans.append(2)

        for i in range(1, lim):
            for j in range(0, i):
                if A[i] - A[j] in d[j]:
                    d[i][A[i] - A[j]] = d[j][A[i] - A[j]] + 1
                    if d[i][A[i] - A[j]] > ans[i]:
                        ans[i] = d[i][A[i] - A[j]]

                else:
                    d[i][A[i] - A[j]] = 2
        # print(d)
        return max(ans)
