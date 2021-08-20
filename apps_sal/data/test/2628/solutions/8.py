class Solution:

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 0:
            return []
        elif n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        result = [0, 1]
        res_len = 2 ** n
        cnt = 1
        while len(result) != res_len:
            cnt *= 2
            result.extend(result[::-1])
            offset = 0
            for i in range(len(result)):
                if i > 0 and i % cnt == 0:
                    offset = cnt
                result[i] += offset
        return result
