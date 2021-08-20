class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def revert(s):
            ans = ''
            for x in s:
                if x == '1':
                    ans += '0'
                else:
                    ans += '1'
            return ans

        def helper(n):
            if n == 1:
                return '0'
            res = helper(n - 1)
            return res + '1' + revert(res)[::-1]
        return helper(n)[k - 1]
