class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        def getLength(orgprev, orgcurr, prev, curr):
            nxt = curr + prev
            if nxt in Aset:
                return 1 + getLength(orgprev, orgcurr, curr, nxt)
            else:
                return 2 if orgprev != prev and orgcurr != curr else 0
        Aset = set(A)
        return max(max([getLength(a, b, a, b) for a in A[:i]], default=float('-inf')) for i, b in enumerate(A))
