class Solution:

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ''
        dic = {}
        for i in t:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        counter = len(dic)
        start = end = 0
        minl = len(s) + 1
        res = ''
        while end < len(s):
            j = s[end]
            if j in dic:
                dic[j] -= 1
                if dic[j] == 0:
                    counter -= 1
            end += 1
            while counter == 0:
                i = s[start]
                if i in dic:
                    dic[i] += 1
                    if dic[i] > 0:
                        counter += 1
                    if end - start < minl:
                        minl = end - start
                        res = s[start:end]
                start += 1
        return res
