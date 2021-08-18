class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for x in data:
            if count == 0:
                if x >> 5 == 0b110:
                    count = 1
                elif x >> 4 == 0b1110:
                    count = 2
                elif x >> 3 == 0b11110:
                    count = 3
                elif x >> 7 == 1:
                    return False
            else:
                if x >> 6 != 0b10:
                    return False
                count -= 1
        return count == 0
