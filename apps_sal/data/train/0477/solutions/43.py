class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inverse(s):
            res = ''
            for ch in s:
                if ch == '1':
                    res += '0'
                else:
                    res += '1'
            return res

        s = '0'
        for i in range(n - 1):
            s = s + '1' + inverse(s)[::-1]
        return s[k - 1]
