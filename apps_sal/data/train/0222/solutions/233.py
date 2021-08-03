class Solution:
    def lenLongestFibSubseq(self, A):
        sA = set(A)
        last = A[-1]
        B = Counter()
        best = 0
        for i in reversed(range(len(A))):
            a = A[i]
            for b in A[i + 1:]:
                c = a + b
                if c in sA:
                    B[a, b] = 1 + B[b, c]
                    best = max(best, B[a, b] + 2)
                elif c > last:
                    break
        return best
