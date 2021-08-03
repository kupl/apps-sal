class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        indices = {n: i for i, n in enumerate(A)}
        d = defaultdict(lambda: 2)
        ans = 0
        for k, n in enumerate(A):
            for j in range(k - 1, 0, -1):
                m = n - A[j]
                if m not in indices:
                    continue
                i = indices[m]
                if i >= j:
                    break
                d[k, j] = d[j, i] + 1
                ans = max(ans, d[k, j])
        return ans
