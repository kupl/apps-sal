class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        res, flipped, isFlipped = 0, 0, [0] * len(A)

        for i in range(len(A)):
            if i >= K:
                flipped ^= isFlipped[i - K]
            if not A[i] ^ flipped:
                if i + K > len(A):
                    return -1
                isFlipped[i] ^= 1
                res += 1
                flipped ^= 1

        return res
