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
                    B[a, b] = B[b, c] + 1  # if recording B[b,c], everything is counted 1. We are tracking back like 3+5, 2+3, 1+2. So we want the 1+2 to be counted the most.
                    ans = max(ans, B[a, b] + 2)  # [a, b, c] = [1 ,2, 3], B[b, c] = 1
                if c > A[-1]:
                    break  # the inner loop needn't continue
        return ans if ans >= 3 else 0
