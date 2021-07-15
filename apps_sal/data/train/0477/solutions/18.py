class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        x = '0'
        for i in range(1, n):
            x = x + '1' + ''.join(list(map(lambda x: '1' if x == '0' else '0', x))[::-1])
        return x[k-1]
