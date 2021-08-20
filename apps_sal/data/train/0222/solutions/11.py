class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x: i for (i, x) in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)
        ans = 0
        for (i, a) in enumerate(A):
            for j in range(i):
                k = index.get(a - A[j], None)
                if k is not None and k < j:
                    cand = longest[j, i] = longest[k, j] + 1
                    ans = max(cand, ans)
        return ans
