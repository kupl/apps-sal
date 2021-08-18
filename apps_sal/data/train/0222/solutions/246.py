class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        val2idx = {val: i for i, val in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)
        longest[(0, 0)] = 1
        res = 0
        for k in range(2, len(A)):
            for j in range(k):
                i = val2idx.get(A[k] - A[j], None)
                if i != None and i < j:
                    longest[(j, k)] = longest[(i, j)] + 1
                    res = max(res, longest[(j, k)])
        return res if res >= 3 else 0
