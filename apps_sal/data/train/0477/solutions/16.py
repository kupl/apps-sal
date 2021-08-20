class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        s = []
        s.append('0')
        for i in range(1, n):
            ans = s[i - 1] + '1'
            temp = ''
            for j in s[i - 1]:
                if j == '0':
                    temp += '1'
                else:
                    temp += '0'
            ans = ans + temp[::-1]
            s.append(ans)
        return s[-1][k - 1]
