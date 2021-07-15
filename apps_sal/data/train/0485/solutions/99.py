class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        tot = 0
        flips = []
        mask = 0
        for i in range(len(A) - (K - 1)):
            if flips and i == flips[0]:
                flips.pop(0)
                mask ^= 1
            if A[i] == mask:
                flips.append(i + K)
                tot += 1
                mask ^= 1
        for i in range(len(A) - K, len(A)):
            if flips and i == flips[0]:
                flips.pop(0)
                mask ^= 1
            if A[i] == mask:
                return -1
        return tot

