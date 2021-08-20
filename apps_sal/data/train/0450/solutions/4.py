class Solution:

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for num in data:
            if count == 0:
                if num >> 5 == 6:
                    count = 1
                elif num >> 4 == 14:
                    count = 2
                elif num >> 3 == 30:
                    count = 3
                elif num >> 7:
                    return False
            else:
                if num >> 6 != 2:
                    return False
                count -= 1
        return count == 0
