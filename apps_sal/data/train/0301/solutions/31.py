class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if len(A) < len(B):
            A, B = B, A
        n = len(B)
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            if A[0] == B[i - 1]:
                prev[i] = 1
            else:
                prev[i] = prev[i - 1]
        curr = [0] * (n + 1)
        for i in range(1, len(A)):
            for j in range(1, n + 1):
                if A[i] == B[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(curr[j - 1], prev[j])
            prev, curr = curr, prev
        return prev[-1]
