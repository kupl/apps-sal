
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        #return sorted(map(lambda x: (self.myfunc(x),x), range(lo,hi+1)) )[k-1][1]
        return sorted([(self.recursive(x,0,{}),x) for x in range(lo,hi+1)] )[k-1][1]


    
    def recursive(self, x, count,memo):
        if x in memo:
            return memo[x]
        elif x==1:
            memo[x]=count
            return count
        elif x%2==0:
            return self.recursive(x/2, count+1, memo)
        else:
            return self.recursive(3*x+1, count+1, memo)
        
        

