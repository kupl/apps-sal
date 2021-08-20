class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        maxVal = 1
        cur = collections.defaultdict(dict)
        for (i, val) in enumerate(A):
            for j in range(i):
                dist = A[i] - A[j]
                cur[i][dist] = 1 + cur[j].get(dist, 1)
                maxVal = max(maxVal, cur[i][dist])
        return maxVal
