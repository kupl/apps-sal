class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:

        def checksign(A, B):
            if A > B:
                return 1
            if A < B:
                return -1
            if A == B:
                return 0
        n = len(A)
        ans = 1
        start = 0
        for i in range(1, n):
            if checksign(A[i - 1], A[i]) == 0:
                start = i
            if i == n - 1:
                ans = max(ans, i - start + 1)
                break
            if checksign(A[i - 1], A[i]) * checksign(A[i], A[i + 1]) != -1:
                ans = max(ans, i - start + 1)
                start = i
        return ans
