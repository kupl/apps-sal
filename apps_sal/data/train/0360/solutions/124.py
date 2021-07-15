class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n=len(weights)
        l=max(weights)
        r=n*max(weights)
        pre=[weights[0]]
        for i in range(1,len(weights)):
            pre.append(pre[-1]+weights[i])
        def checker(val) -> bool:
            x=0
            y=0
            j=0
            i=0
            while(i<len(pre)):
                x=pre[i]-y
                if(x==val):
                    x=0
                    y=pre[i]
                    j+=1
                    if(j>D):
                        return False
                elif(x>val):
                    x=0
                    y=pre[i-1]
                    i-=1
                    j+=1
                    if(j>D):
                        return False
                i+=1
            if(j==D)and(x!=0):
                return False
            return True
        while(l<r):
            mid=(l+r)//2
            if(checker(mid)==True):
                r=mid
            else:
                l=mid+1
        return l
        
            

