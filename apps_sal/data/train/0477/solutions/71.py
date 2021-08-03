class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        curr = '0'
        for x in range(2, n + 1):
            nxt = curr + '1' + self.invert(curr)[::-1]
            curr = nxt
        return curr[k - 1]

    def invert(self, s):
        return ''.join(['1' if x == '0' else '0' for x in s])
