class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        d = [{}]
        ans = 0
        for i in range(1, len(A)):
            d.append({})
            for j in range(i):
                if (A[j] - A[i]) in d[j]:
                    d[i][A[j] - A[i]] = d[j][A[j] - A[i]] + 1
                else:
                    d[i][A[j] - A[i]] = 1
                ans = max(ans, d[i][A[j] - A[i]])
        return ans + 1
