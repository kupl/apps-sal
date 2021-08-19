class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x: i for (i, x) in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)
        ans = 0
        for (k, c) in enumerate(A):
            for j in range(k - 1, -1, -1):
                if A[j] <= c // 2:
                    break
                i = index.get(c - A[j], None)
                if i is not None:
                    cand = longest[A[j], c] = longest[A[i], A[j]] + 1
                    ans = max(ans, cand)
        return ans if ans >= 3 else 0
