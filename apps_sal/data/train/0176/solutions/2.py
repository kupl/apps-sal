class Solution:
    def __init__(self):
        self.maps = {}

    def isScramble(self, s1, s2):
     #   print(s1, s2)
        if (s1, s2) in self.maps:
            return self.maps[(s1, s2)]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.maps[(s1, s2)] = False
            return False
        if s1 == s2:
            self.maps[(s1, s2)] = True
            return True
        n = len(s1)
        for sz in range(1, n):
            if ((self.isScramble(s1[:sz], s2[:sz]) and self.isScramble(s1[sz:], s2[sz:]))
               or (self.isScramble(s1[:sz], s2[-sz:]) and self.isScramble(s1[sz:], s2[:-sz]))):
                self.maps[(s1, s2)] = True
                return True
        self.maps[(s1, s2)] = False
        return False
