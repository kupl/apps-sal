class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ls = [1, 10, 91]
        mul = 9

        res = 0
        for i in range(8):
            mul = 9
            m = 9
            for j in range(i + 2):
                mul *= m
                m -= 1
            # print(mul)
            ls.append(mul + ls[-1])
        if n >= 9:
            return ls[9]
        else:
            return ls[n]
