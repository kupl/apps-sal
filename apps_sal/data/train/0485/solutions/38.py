class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        res = 0
        flip = 0
        na = [0]*len(A)
        for i,x in enumerate(A):
            flip ^= na[i]
            if flip ^ x == 0:
                res += 1
                flip ^= 1
                if i+ K > len(A):
                    return -1
                if i+ K < len(A):
                    na[i+K] ^= 1
        return res
