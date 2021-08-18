class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        cipher = dict((str(k + 1), v) for k, v in
                      enumerate("abcdefghijklmnopqrstuvwxyz"))
        funhash = {"": 1}

        def helpRec(s):
            if s in funhash:
                return funhash[s]
            r1 = 0
            if s[0] in cipher:
                r1 = helpRec(s[1:])
            r2 = 0
            if len(s) >= 2 and s[:2] in cipher:
                r2 = helpRec(s[2:])
            rval = r1 + r2
            funhash[s] = rval
            return rval
        return helpRec(s)
