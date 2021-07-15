class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        s = set(A)
        if n <= 2:
            return 0
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                a, b = A[j], A[i] + A[j]
                count = 2
                while b in s:
                    count += 1
                    a, b = b, a + b
                if count > 2:
                    ans = max(ans, count)
        return ans
