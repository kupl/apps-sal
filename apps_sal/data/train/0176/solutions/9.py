class Solution:

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True
        for i in range(len(s1) - 1):
            if self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:]) or (self.isScramble(s1[:i + 1], s2[len(s1) - i - 1:]) and self.isScramble(s1[i + 1:], s2[:len(s1) - i - 1])):
                return True
        return False
