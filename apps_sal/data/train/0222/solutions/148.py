class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        indexes = {x:i for i, x in enumerate(A)}
        longest = defaultdict(lambda: 1)
        for i in range(1, N):
            for j in range(i):
                k = indexes.get(A[i] - A[j], -1)
                longest[(i, j)] = longest[(j, k)] + 1
        # print(longest)
        longest = max(longest.values())
        return longest if longest >= 3 else 0

