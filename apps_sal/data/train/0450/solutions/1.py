class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for d in data:
            if count == 0:
                if d >> 5 == 0b110:
                    count = 1
                elif d >> 4 == 0b1110:
                    count = 2
                elif d >> 3 == 0b11110:
                    count = 3
                elif d >> 7 != 0:
                    return False
            else:
                if d >> 6 == 0b10:
                    count -= 1
                else:
                    return False
        return count == 0
