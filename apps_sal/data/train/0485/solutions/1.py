
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        l = len(A)
        flipped = [0] * l
        res = 0
        flipping_count = 0
        for i in range(l):
            if i >= K:
                flipping_count -= flipped[i - K]
            if (flipping_count % 2 == 0 and A[i] == 0) or (flipping_count % 2 == 1 and A[i] == 1):
                if i + K > l:
                    return -1
                flipped[i] += 1
                flipping_count += 1
                res += 1
                
        return res
