class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        d = {}
        for i in range(len(A)):
            d[A[i]] = i

        ans = 0
        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                y = A[i] + A[j]
                x = A[j]
                l = 2
                while y in d and d[y] > j:
                    z = x + y
                    x = y
                    y = z
                    l += 1
                ans = max(ans, l)
        return ans if ans >= 3 else 0
