class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        cur = collections.defaultdict(dict)
        maxSeq = 0
        for (i, v) in enumerate(A):
            for j in range(i):
                val = v - A[j]
                cur[i][val] = 1 + cur[j].get(val, 1)
                if maxSeq < cur[i][val]:
                    maxSeq = cur[i][val]
        return maxSeq
