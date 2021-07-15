from collections import defaultdict as d
class Solution:
    MAXPRIME=100001
    isPrime=[0 for _ in range(MAXPRIME+1)]
    isPrime[0]=-1;isPrime[1]=-1 #0 and 1 are not prime numbers
    for i in range(2,MAXPRIME//2):
        if isPrime[i]==0: #i is prime
            for multiple in range(i*i,MAXPRIME+1,i):
                if isPrime[multiple]==0:
                    isPrime[multiple]=i         
    def largestComponentSize(self, A: List[int]) -> int:
        arr=A
        n=len(arr)
        
        primeConnections=d(set) #primeConnections[i]={connected prime numbers}
        primeFactorCnts=d(lambda:0)
        
        for x in arr:
            if x==1:continue
            primeFactors=set()
            while Solution.isPrime[x]!=0:
                primeFactors.add(Solution.isPrime[x])
                x//=Solution.isPrime[x]
            primeFactors.add(x)
            primeFactors=list(primeFactors)
            if len(primeFactors)>0:
                primeFactorCnts[primeFactors[0]]+=1 #only increment the smallest prime factor since all the prime factors will be linked
                for i in range(len(primeFactors)-1):
                    for j in range(i+1,len(primeFactors)):
                        primeConnections[primeFactors[i]].add(primeFactors[j]) #create links between all prime factors for the number
                        primeConnections[primeFactors[j]].add(primeFactors[i])
        
        def dfs(p,componentSize): #find the total size of each component
            exploredSet.add(p)
            componentSize[0]+=primeFactorCnts[p]
            for nex in primeConnections[p]:
                if nex not in exploredSet:
                    dfs(nex,componentSize)
                    
        connectedComponentsSizes=[]
        exploredSet=set()
        for p in primeConnections.keys():
            if p not in exploredSet:
                componentSize=[0]
                dfs(p,componentSize)
                connectedComponentsSizes.append(componentSize[0])
        ans=max(connectedComponentsSizes)
        return ans
