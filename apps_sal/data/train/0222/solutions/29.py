class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        idxs = {x: i for i, x in enumerate(A)}
        longest = defaultdict(lambda: 2)

        res = 0
        for k, val in enumerate(A):
            for j in range(k):
                i = idxs.get(val - A[j], None)
                if i is not None and i < j:
                    candidate = longest[(j, k)] = longest[(i, j)] + 1
                    res = max(res, candidate)
        return res if res >= 3 else 0
