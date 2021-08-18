class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        result = [0, 1]

        for i in range(2, n + 1):
            mask = 1 << (i - 1)
            temp = []
            for j in range(len(result)):
                temp.append(result[-j - 1] | mask)
            result += temp
        return result
