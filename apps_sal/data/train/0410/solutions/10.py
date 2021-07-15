class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d   =   {}
        for i in range(lo,hi+1):
            self.pow(i,i,d,0)
            #print(d)
        d1  =   OrderedDict(sorted(list(d.items()),key=lambda x:x[1]))
        l   =   list(d1.keys())
        return l[k-1]
            
    def pow(self,n1,n,d,c):
        if n    ==  1:
            d[n1]   =   c
            return 
        if  n%2 ==0:
            n   =   n/2
        elif n%2    ==  1:
            n   =   n*3 +   1
        c   +=  1
        if n in d:
            d[n1]   =   c   +   d[n]
            return
        self.pow(n1,n,d,c)
        
            
            

