class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def parsePatern(p):
            pi = len(p) - 1
            while pi >= 0:
                if p[pi] == '*':
                    if pi == 0:
                        raise Exception('Invalid pattern!')
                    yield (p[pi - 1], 1)
                    pi -= 2
                else:
                    yield (p[pi], 0)
                    pi -= 1
        from collections import deque
        if not p:
            return p == s
        plist = list(parsePatern(p))
        P = len(plist)
        q = set([(0, len(s) - 1)])
        seen = set()
        "\n         q = [ (('a',1), 4) ]\n         q = [ (('b',1), 4), (('b',1), 3) ] \n         q = [ (('a', 0), 4), (('a',0), 3)), (('a',0), 2), (('a',0), 1), (('a',0), 0), (('a',0), -1)]\n         q = [ (('b', 0), 3) ]\n         q = [ (('b', 1), 2)]\n         q = [ (('', 0), 2), (('', 0), 1), (('', 0), 0), (('', 0), -1)]\n         (('', 0), -1)-> true\n         \n         "
        while q:
            (pat_i, si) = q.pop()
            if (pat_i, si) in seen:
                continue
            seen.add((pat_i, si))
            (pat, is_as) = plist[pat_i] if pat_i < P else ('', 0)
            "\n             1. a, 1\n                 1: bbbb\n                 0: bbbba\n             2. b, 1\n                 10: bbbb\n                 11: bbb\n                 12: bb\n                 13: b\n                 14: ''\n                 00: bbbba\n             3. a, 0\n                 001: bbbb\n             4. b, 0\n                 0011: bbb\n             5, b, 1:\n                 00110: bbb\n                 00111: bb\n                 00112: b\n                 00113: ''\n             6, '', 0\n                 00113 -> true\n             "
            if not pat and si < 0:
                return True
            if is_as:
                q.add((pat_i + 1, si))
                while si >= 0 and (s[si] == pat or pat == '.'):
                    si -= 1
                    q.add((pat_i + 1, si))
            elif si >= 0 and (s[si] == pat or pat == '.'):
                q.add((pat_i + 1, si - 1))
        return False
