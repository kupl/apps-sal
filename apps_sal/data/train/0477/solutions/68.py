class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        cur = '0'
        
        while len(cur) < k:
            cur = cur + '1' + ''.join('1' if b == '0' else '0' for b in reversed(cur))
            
        return cur[k-1]
