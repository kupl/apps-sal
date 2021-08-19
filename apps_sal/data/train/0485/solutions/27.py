class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        num = 0
        for a in A:
            num = (num << 1) + a
        i = 0
        pattern = (1 << K) - 1
        flips = 0
        while i + K <= len(A):
            while i + K <= len(A) and num & 1 << i:
                i += 1
            if i + K > len(A):
                break
            num ^= pattern << i
            flips += 1
            i += 1
        if num == (1 << len(A)) - 1:
            return flips
        return -1
