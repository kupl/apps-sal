class Solution:
    def getProbability(self, balls: List[int]) -> float:
        firsthalf, secondhalf = [0]*len(balls),[0]*len(balls)
        self.good, self.all = 0,0
        
        @lru_cache(None)
        def fac(n):
            if n==0:
                return 1
            return n*fac(n-1)
        
        def permutation(arr):
            prod = 1
            for v in arr:
                prod*=fac(v)
            return fac(sum(arr))/prod
        def dfs(i):
            if i == len(balls):
                if sum(firsthalf)!=sum(secondhalf):
                    return 
                p1,p2 = permutation(firsthalf),permutation(secondhalf)
                self.all+=p1*p2
                self.good +=p1*p2 if sum(v>0 for v in firsthalf)==sum(v>0 for v in secondhalf) else 0
            else:
                for j in range(balls[i]+1):
                    firsthalf[i],secondhalf[i]=j, balls[i]-j
                    dfs(i+1)
        dfs(0)
        return self.good/self.all
