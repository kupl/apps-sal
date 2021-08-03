class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        result = ''
        for word in d:
            lo = 0
            for l in word:
                lo = s.find(l, lo) + 1
                if lo == 0:
                    break
            if lo > 0 and len(word) >= len(result):
                if len(word) == len(result):
                    result = word if word < result else result
                else:
                    result = word
        return result
