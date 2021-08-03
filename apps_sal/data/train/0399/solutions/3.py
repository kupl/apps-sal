class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        char_code = {k: str(v) for k, v in zip(alphabet, list(range(1, 27)))}
        code_char = {v: k for k, v in list(char_code.items())}

        def numDecodingsHelper(s, hist={}):
            if not s:
                return 0
            if len(s) == 1:
                return 1 if s in code_char else 0
            if len(s) == 2:
                tmp = 1 if s in code_char else 0
                return tmp + numDecodingsHelper(s[0]) * numDecodingsHelper(s[1])
            if s[1:] not in hist:
                hist[s[1:]] = numDecodingsHelper(s[1:], hist)
            current1 = hist[s[1:]] if s[:1] in code_char else 0
            if s[2:] not in hist:
                hist[s[2:]] = numDecodingsHelper(s[2:], hist)
            current2 = hist[s[2:]] if s[:2] in code_char else 0
            return current1 + current2
        return numDecodingsHelper(s, {})
