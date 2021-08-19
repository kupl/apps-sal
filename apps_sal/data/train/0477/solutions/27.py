class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def negVal(val):
            lenVal = len(val)
            mask = int('1' * lenVal, 2)
            val = int(val, 2)
            neg = val ^ mask
            lenNeg = len(bin(neg)) - 2
            neg = '0' * (lenVal - lenNeg) + bin(neg)[2:]
            return neg[::-1]
        strVal = '0'
        for i in range(n - 1):
            strVal += '1' + negVal(strVal)
        if k > len(strVal):
            return '0'
        else:
            return strVal[k - 1]
