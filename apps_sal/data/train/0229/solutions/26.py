class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        if not A:
            return True
        d=defaultdict(int)
        for x in A:
            d[x]+=1
        n=len(A)//2
        A.sort()
        for x in A:
            if d[x]>0:
                if 2*x in d and d[2*x]>0:
                    d[2*x]-=1
                    d[x]-=1
                    n-=1
                    if n==0:
                        return True
            #print(x,d,n)
        return False
                
        

