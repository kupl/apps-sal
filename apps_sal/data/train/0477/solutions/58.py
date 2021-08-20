class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for i in range(2, n + 1):
            sRevInv = ''.join(['1' if c == '0' else '0' for c in s[::-1]])
            s = s + '1' + sRevInv
            if len(s) >= k:
                break
        return s[k - 1]
