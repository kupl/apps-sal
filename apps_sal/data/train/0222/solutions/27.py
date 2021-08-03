class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        def getLength(prev, curr):
            nxt = curr + prev
            if nxt in Aset:
                return 1 + getLength(curr, nxt)
            else:
                return 2
        Aset = set(A)
        out = max(max([getLength(a, b) for a in A[:i]], default=float('-inf')) for i, b in enumerate(A))
        return out if out >= 3 else 0
