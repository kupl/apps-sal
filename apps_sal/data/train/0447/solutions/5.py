class Solution:
    def removeDuplicateLetters(self, s):
        ret = ''
        while s:
            p = min(s.rindex(c) for c in set(s))
            c = min(s[:p + 1])
            ret += c
            s = s[s.index(c):].replace(c, '')
        return ret
