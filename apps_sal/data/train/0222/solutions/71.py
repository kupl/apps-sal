class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        mapA = {n: i for i, n in enumerate(A)}

        # 1. Brutal Force
        l = ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                x, y = A[j], A[i] + A[j]
                l = 2
                while y in mapA:
                    x, y = y, x + y
                    l += 1
                ans = max(ans, l)
        return ans if ans >= 3 else 0
