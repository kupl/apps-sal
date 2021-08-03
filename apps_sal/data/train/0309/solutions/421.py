class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        result = 1
        n = len(A)
        umap = [dict() for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                jval = (umap[j][diff] if diff in umap[j] else 0)
                if diff not in umap[i]:
                    umap[i][diff] = 0
                umap[i][diff] = max(umap[i][diff], jval + 1)
                result = max(result, umap[i][diff])
        return result + 1
