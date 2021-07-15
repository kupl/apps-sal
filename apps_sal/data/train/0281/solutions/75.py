class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        d = {}
        if(len(s)!= len(t)):
            return False
        for i in range(len(s)):
            if(s[i]!= t[i]):
                if(ord(s[i])<ord(t[i])):
                    val = ord(t[i])-ord(s[i])
                else:
                    val = (ord('z')-ord(s[i]))+(ord(t[i])-ord('a'))+1
                if(val in d):
                    d[val]+=1
                elif(val not in d):
                    d[val] = 1
        for x in d:
            if(((d[x]-1)*26+x)>k):
                return False
        return True
