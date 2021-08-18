class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length_1 = len(s1)
        length_2 = len(s2)
        if length_1 > length_2:
            return False
        S1_MAP = [0] * 128
        S2_MAP = [0] * 128

        for char in s1:
            S1_MAP[ord(char)] += 1
        index = 0
        while index < length_1 - 1:
            S2_MAP[ord(s2[index])] += 1
            index += 1
        while index < length_2:
            S2_MAP[ord(s2[index])] += 1
            if index >= length_1:
                S2_MAP[ord(s2[index - length_1])] -= 1
            if S1_MAP == S2_MAP:
                return True
            index += 1
        return False
