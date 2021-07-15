class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t):
            return False
        hash={}

        n=len(s)

        for i in range(n):
            x=ord(t[i])-ord(s[i])
            if x==0:
                continue
            if x>0:
                if x in hash:
                    hash[x]+=[x+26*(len(hash[x]))]
                else:
                    hash[x]=[x]
            elif x<0:
                if 26+x in hash:
                    hash[26+x]+=[26+x+26*(len(hash[26+x]))]
                else:
                    hash[26+x]=[26+x]
        for a in hash:
            if a>k:
                return False
            for i in hash[a]:
                if i>k:
                    return False
        return True                
