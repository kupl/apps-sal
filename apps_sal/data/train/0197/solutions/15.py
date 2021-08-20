class Solution:

    def isValid(self, s: str) -> bool:
        dic = collections.defaultdict(list)
        for (i, c) in enumerate(s):
            dic[c].append(i)
        t = ''
        for i in dic['a']:
            t = t[:i] + 'abc' + t[i:]
        return t == s
