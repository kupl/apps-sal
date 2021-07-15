class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        cur = collections.defaultdict(dict)
        for i, v in enumerate(A):
            for j in range(i):
                val = v - A[j]
                cur[i][val] = 1 + cur[j].get(val, 1)
        return max(cur[i][j] for i in cur for j in cur[i])
