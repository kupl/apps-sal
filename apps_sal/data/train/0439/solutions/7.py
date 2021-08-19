class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        l = len(A)
        if l < 1:
            return 0
        elif l == 1:
            return 1
        ans = 1
        start = 0
        cnt = 1

        def cmp(a, b):
            return (a > b) - (a < b)
        while cnt < l:
            if A[cnt - 1] == A[cnt]:
                start = cnt
            elif cnt == l - 1 or cmp(A[cnt - 1], A[cnt]) * cmp(A[cnt], A[cnt + 1]) != -1:
                ans = max(ans, cnt - start + 1)
                start = cnt
            cnt += 1
        return ans
