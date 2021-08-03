class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(x):
            return [0 if i == 1 else 1 for i in x]

        S = [0]
        i = 1

        while i < n and len(S) < k:
            S.append(1)
            S.extend((invert(S[:-1])[::-1]))
            i += 1

        return str(S[k - 1])
