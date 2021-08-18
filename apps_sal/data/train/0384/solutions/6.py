class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:

        aa = sorted(A)
        n = len(A)
        res = 0
        md = 10**9 + 7
        p2 = [1] * n
        for i in range(1, n):
            p2[i] = (p2[i - 1] * 2) % md
        for i in range(n):
            res = (res + aa[i] * (p2[i] - p2[n - i - 1])) % md
        return res
