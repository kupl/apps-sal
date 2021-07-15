class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        indices = {n: i for i, n in enumerate(A)}
        d = defaultdict(lambda: 2)
        ans = 0
        for k, n in enumerate(A):
            for j in range(k-1, 0, -1):
                if (m := n - A[j]) not in indices:
                    continue
                if (i := indices[m]) >= j:
                    break
                d[j, k] = d[i, j] + 1
                ans = max(ans, d[j, k])
        return ans
