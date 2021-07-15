class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d={}
        count=0

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1

        for i in range(len(t)):
            if t[i] in d and d[t[i]] > 0:
                d[t[i]]-=1
            else:
                count+=1

        return count
