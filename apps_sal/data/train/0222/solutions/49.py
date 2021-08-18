class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        sA = set(A)
        B = Counter()
        ans = 0
        for i in reversed(range(len(A))):

            a = A[i]
            for b in A[i + 1:]:
                c = a + b
                if c in sA:
                    B[a, b] = B[b, c] + 1
                    ans = max(ans, B[a, b] + 2)
                if c > A[-1]:
                    break
        return ans if ans >= 3 else 0
