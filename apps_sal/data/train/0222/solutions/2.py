class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x: i for (i, x) in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)
        ans = 0
        for (k, c) in enumerate(A):
            for j in range(k - 1, k // 2 - 2, -1):
                i = index.get(c - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)
        return ans if ans >= 3 else 0
