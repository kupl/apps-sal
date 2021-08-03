class Solution:
    def minKBitFlips(self, A, K: int) -> int:
        flipped, res = 0, 0
        length = len(A)
        isFlipped = [0] * length
        for i, v in enumerate(A):
            if i >= K:
                flipped ^= isFlipped[i - K]
            if flipped == v:
                if i + K > length:
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                res += 1
        return res
