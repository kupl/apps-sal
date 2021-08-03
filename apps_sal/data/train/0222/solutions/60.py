class Solution(object):
    def lenLongestFibSubseq(self, A):
        S = set(A)
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                x, y = A[j], A[i] + A[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0
