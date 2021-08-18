class Solution:
    def __init__(self):
        self.dp = {}
        self.s = ""
        self.t = ""
        self.letter2Indices = {}

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0
        if not t:
            return 1

        self.s = s.lower()
        self.t = t.lower()
        length = len(s)
        for i in range(len(t)):
            self.dp[i] = [-1] * length
        for i in range(length):
            letter = self.s[i]
            if letter in self.letter2Indices:
                self.letter2Indices[letter].append(i)
            else:
                self.letter2Indices[letter] = list([i])

        return self.numSubseq(0, 0)

    def numSubseq(self, startS, startT):
        if startT >= len(self.t):
            return 1
        if startS >= len(self.s):
            return 0

        if self.dp[startT][startS] >= 0:
            return self.dp[startT][startS]

        letter = self.t[startT]
        count = 0
        firstMatch = -1
        if letter in self.letter2Indices:
            for i in self.letter2Indices[letter]:
                if i >= startS:
                    count += self.numSubseq(i + 1, startT + 1)
                    if firstMatch < 0:
                        firstMatch = i

        self.dp[startT][startS] = count
        for i in range(startS + 1, firstMatch):
            self.dp[startT][i] = count
        return count
