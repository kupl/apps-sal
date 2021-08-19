class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        Mod = 1000000000.0 + 7
        n = len(A)
        twoPower = [1]
        while len(twoPower) < n:
            twoPower.append(twoPower[len(twoPower) - 1] * 2 % Mod)
        A.sort()
        ans = 0
        for (i, a) in enumerate(A):
            left = i
            right = n - i - 1
            ans = (ans + (twoPower[left] - twoPower[right]) * a) % Mod
        return int((ans + Mod) % Mod)
