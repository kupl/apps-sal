class Solution:

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for x in data:
            if count == 0:
                if x >> 5 == 6:
                    count = 1
                elif x >> 4 == 14:
                    count = 2
                elif x >> 3 == 30:
                    count = 3
                elif x >> 7 == 1:
                    return False
            else:
                if x >> 6 != 2:
                    return False
                count -= 1
        return count == 0
