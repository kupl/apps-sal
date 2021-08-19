class Solution:

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return list()
        if rowIndex == 0:
            return list([1])
        l = list([1])
        for i in range(1, rowIndex + 1):
            pre_value = l[0]
            for j in range(1, i):
                temp = l[j]
                l[j] = pre_value + l[j]
                pre_value = temp
            l.append(1)
        return l
