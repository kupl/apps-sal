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
        res = '0'
        for _ in range(n):
            res += '1' + invert(res)[::-1]
        return res[k - 1]
