class Solution:

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        def isMatch(s, w):
            index = 0
            for c in w:
                if c in s:
                    index = s.find(c, index) + 1
                    if index == 0:
                        return False
                else:
                    return False
            return True
        candidates = []
        for word in d:
            if isMatch(s, word):
                candidates.append(word)
        candidates = sorted(candidates, key=lambda w: (len(w), w))
        if not candidates:
            return ''
        else:
            maxLen = len(candidates[-1])
            for c in candidates:
                if len(c) == maxLen:
                    return c
