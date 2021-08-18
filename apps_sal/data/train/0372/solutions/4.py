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
        """
         q = [ (('a',1), 4) ]
         q = [ (('b',1), 4), (('b',1), 3) ] 
         q = [ (('a', 0), 4), (('a',0), 3)), (('a',0), 2), (('a',0), 1), (('a',0), 0), (('a',0), -1)]
         q = [ (('b', 0), 3) ]
         q = [ (('b', 1), 2)]
         q = [ (('', 0), 2), (('', 0), 1), (('', 0), 0), (('', 0), -1)]
         (('', 0), -1)-> true
         
         """
        while q:
            pat_i, si = q.pop()
            if (pat_i, si) in seen:
                continue

            seen.add((pat_i, si))
            pat, is_as = plist[pat_i] if pat_i < P else ('', 0)
            """
             1. a, 1
                 1: bbbb
                 0: bbbba
             2. b, 1
                 10: bbbb
                 11: bbb
                 12: bb
                 13: b
                 14: ''
                 00: bbbba
             3. a, 0
                 001: bbbb
             4. b, 0
                 0011: bbb
             5, b, 1:
                 00110: bbb
                 00111: bb
                 00112: b
                 00113: ''
             6, '', 0
                 00113 -> true
             """
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
