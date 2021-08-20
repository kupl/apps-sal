class Solution:

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for d in data:
            if count == 0:
                if d >> 5 == 6:
                    count = 1
                elif d >> 4 == 14:
                    count = 2
                elif d >> 3 == 30:
                    count = 3
                elif d >> 7 != 0:
                    return False
            elif d >> 6 == 2:
                count -= 1
            else:
                return False
        return count == 0
