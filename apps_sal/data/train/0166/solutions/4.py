# a, b, c (i subscript)
# c = 0
# -> a + b = 2 -> 2 flips
# -> a + b = 1 -> 1 flip
# -> a + b = 0 -> 0 flips
# c = 1
# -> a + b = 2 -> 0 flips
# -> a + b = 1 -> 0 flips
# -> a + b = 0 -> 1 flip

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        
        for i in range(32):
            mask = 1 << i
            ai = a & mask
            bi = b & mask
            ci = c & mask
            
            if ci == 0:
                if ai and bi:
                    res += 2
                elif ai or bi:
                    res += 1
            else:
                if not ai and not bi:
                    res += 1
        
        return res

