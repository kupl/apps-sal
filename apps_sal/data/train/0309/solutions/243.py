class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        d = collections.defaultdict(int)
        for i in range(1, len(A)):
            for j in range(i):
                dif = A[i] - A[j]
                if (j, dif) in d:
                    d[i, dif] = d[j, dif] + 1
                else:
                    d[i, dif] = 2
        return max(d.values())
