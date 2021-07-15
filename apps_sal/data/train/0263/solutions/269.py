class Solution:
    
    def knightDialer(self, N: int) -> int:
            
        
        def getNeighbors(N):
            neighs=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
            return neighs[N]
        
        mod= 10**9 +7
        curr= [1]*10
        for i in range(N-1):
            nextlist= [0]*10
            for j in range(10):
                
                for neigh in getNeighbors(j):
                    nextlist[neigh]= (nextlist[neigh]+curr[j])%mod
                    
            curr=nextlist
            
        return sum(curr)%mod
