class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            l = dic.get(s[i],[-1])
            l.append(i)
            dic[s[i]] =l
        res = 0
        for j in dic:
            dic[j].append(len(s))
            for i in range(1, len(dic[j])-1):
                res+= (dic[j][i] - dic[j][i-1])*(dic[j][i+1]-dic[j][i])
        return res%(10**9+7)
