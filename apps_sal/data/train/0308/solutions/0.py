class Solution:

    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """

        def parseTag(src, i):
            j = i
            (tag, i) = findtag(src, i)
            if not tag:
                return (False, j)
            (res, i) = parseContent(src, i)
            e = i + len(tag) + 3
            return (True, e) if src[i:e] == '</' + tag + '>' else (False, j)

        def parseContent(src, i):
            (j, res) = (i, False)
            while i < len(src):
                (res, i) = parseText(src, i)
                if res:
                    continue
                (res, i) = parseCDData(src, i)
                if res:
                    continue
                (res, i) = parseTag(src, i)
                if res:
                    continue
                break
            return (True, i)

        def parseCDData(src, i):
            s = src.find('<![CDATA[', i)
            if s != i:
                return (False, i)
            e = src.find(']]>', i)
            return (True, e + 3) if e != -1 else (False, i)

        def parseText(src, i):
            j = i
            while i < len(src) and src[i] != '<':
                i += 1
            return (j != i, i)

        def findtag(src, i):
            if src[i] != '<':
                return ('', i)
            e = src.find('>', i + 1)
            if e == -1 or e - i - 1 > 9 or e - i - 1 < 1:
                return ('', e)
            s = 1
            while s < e - i and src[i + s].isupper():
                s += 1
            return (src[i + 1:e], e + 1) if s >= e - i else ('', e)
        return parseTag(code, 0) == (True, len(code))
