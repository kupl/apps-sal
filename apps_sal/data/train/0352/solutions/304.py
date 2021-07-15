class Solution:
    def string1(self,s1,s2):
        if  abs(len(s1)-len(s2))>1 or abs(len(s1)-len(s2))==0:
            return False
        i=0
        j=0
        k=0
        while i<len(s1) and j<len(s2):
            if k>1:return False
            if s1[i]!=s2[j]:
                k+=1
                if len(s1)>len(s2):
                    i+=1
                else:
                    j+=1
            else:
                i+=1
                j+=1
        return True if k<=1 else False
    def longestStrChain(self, words: List[str]) -> int:
        words= sorted(words,key=len,reverse=True)
        d={}
        l=len(words[0])
        m=1
        for i in range(len(words)):
            w=words[i]
            m=max([m]+list(d.values()))
            d={key:val for key,val in list(d.items()) if len(key)<=len(w)+1}
            d[w]=1
            for key,val in list(d.items()):
                if self.string1(key,w):
                    d[w]=max(d[w],d[key]+1)
            l=len(w)
        return max([m]+list(d.values()))

