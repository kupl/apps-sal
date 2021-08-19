class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        S = [0]
        for i in range(2, n + 1):
            S += [1] + [1 if i == 0 else 0 for i in S[::-1]]
        return str(S[k - 1])
