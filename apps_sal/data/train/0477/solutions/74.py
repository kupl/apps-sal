class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def helper(res, k):
            if k == 0:
                return res
            invert = ['1' if i == '0' else '0' for i in res]
            invert = ''.join(invert)
            res = res + '1' + invert[::-1]
            return helper(res, k - 1)
        res = helper('0', n - 1)
        return res[k - 1]
