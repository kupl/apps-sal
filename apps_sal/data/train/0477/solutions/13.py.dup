class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(data):
            ans = ''
            for val in data:
                if val == '1':
                    ans += '0'
                else:
                    ans += '1'
            return ans

        res = [''] * (n + 1)
        res[1] = '0'
        for i in range(2, n + 1):
            res[i] = res[i - 1] + '1' + invert(res[i - 1])[::-1]

        return res[n][k - 1]
