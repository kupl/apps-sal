class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def revinv(x):
            ans = []
            for c in x:
                if c == '0':
                    ans.append('1')
                else:
                    ans.append('0')
            return ''.join(reversed(ans))
        s = '0'
        while k > len(s):
            s = s + '1' + revinv(s)
        return s[k - 1]
