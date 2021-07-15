class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        flips = [0] * n
        flip = 0
        ans = 0
        
        def mapping(a: int, flip: int) -> int:
            return 1 - a if flip % 2 == 1 else a
            
        for i, a in enumerate(A):
            flip += flips[i]
            if mapping(a, flip) == 0:
                if i + K - 1 < n:
                    ans += 1
                    flips[i] += 1
                    flip += 1
                    A[i] = 1
                    if i + K < n:
                        flips[i + K] -= 1
                else:
                    return -1
        return ans
