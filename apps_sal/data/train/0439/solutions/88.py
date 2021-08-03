class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        inc = [1 for _ in range(n)]
        dec = [1 for _ in range(n)]

        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                inc[i] = dec[i - 1] + 1
                dec[i] = 1
            elif A[i - 1] > A[i]:
                dec[i] = inc[i - 1] + 1
                inc[i] = 1
            else:
                inc[i] = 1
                dec[i] = 1
        return max(max(inc), max(dec))
