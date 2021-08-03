class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        m = 2 ** n - 1
        if k == 1 or 0 < m - k < 4:
            return '0'
        if k == m or k < 5:
            return '1'
        s = [0]
        for _ in range(n - 1):
            s += [1] + [x ^ 1 for x in reversed(s)]
        return str(s[k - 1])
