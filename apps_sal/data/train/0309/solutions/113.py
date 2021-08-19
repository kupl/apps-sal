class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        mapp = collections.defaultdict(int)
        if not A:
            return -1
        for i in range(1, len(A)):
            for j in range(0, len(A[:i])):
                d = A[i] - A[j]
                if (d, j) in mapp:
                    mapp[d, i] = mapp[d, j] + 1
                else:
                    mapp[d, i] = 2
        return max(mapp.values())
