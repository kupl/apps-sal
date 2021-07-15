class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        # Sliding Window
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # def cmp(a, b):
        #     return (a > b) - (a < b)

        # N, ans, anchor = len(A), 1, 0

        # for i in range(1, N):
        #     c = cmp(A[i - 1], A[i])
        #     if c == 0:
        #         anchor = i
        #     elif i == N - 1 or c * cmp(A[i], A[i + 1]) != -1:
        #         ans = max(ans, i - anchor + 1)
        #         anchor = i

        # return ans


        best = clen = 0
        for i in range(len(A)):
            if i >= 2 and (A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
                clen += 1
            elif i >= 1 and A[i - 1] != A[i]:
                clen = 2
            else:
                clen = 1

            best = max(best, clen)
        return best

