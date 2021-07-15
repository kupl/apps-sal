class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # S的奇数序列是 01010101，(3, 7, 11, ...)是1
        # 所以如果k是奇数，直接返回 (k >> 1) & 1
        
        # S的偶数序列是 1101100... (2, 4, 6, 8, 10, ...)
        # 这个序列的奇数序列是 10101010，(2, 6, 10, 14, ...), (2, 10, 18, ...)是1
        # 所以如果k是偶数，k >> 1就将偶数序列移动到奇数位置上 -> (1, 5, 9, ...)是1
        # 重复这个过程直到k为奇数，然后 (k >> 1) & 1 ^ 1
        
        # k // (k & -k) 相当于除到k为奇数。
        return str((k // (k & -k)) >> 1 & 1 ^ ((k & 1) ^ 1))
    
    def findKthBit_logn(self, n: int, k: int) -> str:
        cur, flip = 1 << (n - 1), 0
        while k > 1:
            if k & (k - 1) == 0:
                return str(flip ^ 1)
            if k > cur:
                k = 2 * cur - k
                flip ^= 1
            cur >>= 1
        
        return str(flip)
