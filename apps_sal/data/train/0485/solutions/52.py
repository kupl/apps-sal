class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flips = 0
        carry = 10
        result = 0
        valid = True
        for i, num in enumerate(A):
            if (A[i] & 1) == (flips & 1):
                result += 1
                flips += 1
                if i < len(A) - K + 1:
                    A[i + K - 1] += carry
                else:
                    valid = False
            if A[i] > 1:
                A[i] -= carry
                flips -= 1

        return result if valid else -1

