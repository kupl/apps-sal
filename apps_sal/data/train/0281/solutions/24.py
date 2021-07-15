class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t):
            return False
        d=defaultdict(int)
        for i in range(len(s)):
            #l.append((ord(t[i])-ord(s[i]))%26)
            n=(ord(t[i])-ord(s[i]))%26
            if n>0:
                d[n]+=1
            
        d2=defaultdict(int)
        kk=k//26
        for i in range(26):
            d2[i+1]=kk
        for i in range(k%26):
            d2[i+1]+=1
        #print(d,d2)
        for k in d:
            if k not in d2 or d[k]>d2[k]:
                return False
        return True

