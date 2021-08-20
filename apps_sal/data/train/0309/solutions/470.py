class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        res = 0
        records = [collections.defaultdict(int) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                current = records[i].get(diff, 0)
                prev = records[j].get(diff, 0) + 1
                records[i][diff] = max(prev, current, 2)
                res = max(res, records[i][diff])
        return res
