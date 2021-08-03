class Solution:
    def removeDuplicateLetters(self, s):
        if not s:
            return ""

        res = ''
        sorted_set = sorted(set(s))

        for c in sorted_set:
            sub_s = s[s.index(c):]
            if set(s) == set(sub_s):
                return c + self.removeDuplicateLetters(sub_s.replace(c, ''))

        return res
