class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {}
        for i in range(lo, hi+1):
            z = self.getTheP(i)
            dic[i] = self.getTheP(i)
        return sorted(list(dic.items()), key=lambda x:(x[1],x[0]))[k-1][0]
            
    def getTheP(self, q: int) -> int:
        Pow = 0
        while (q!= 1):
            if(q%2 == 0):
                q = (q/2)
                Pow+=1
            else:
                q=(3*q+1)
                Pow+=1
        return Pow        
        
        

