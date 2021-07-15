class Solution:
    def knightDialer(self, N: int) -> int:
        
        m,n = 4,3
        
        
        
        dp = {}
        ans = 0
        for k in range(1,N+1):
            count = 0
            for i in range(m):
                for j in range(n):
                    if i==3 and j in [0,2]: continue
                    
                    temp = 0
                            
                    if 1==k:
                        temp+=1

                    else:
                        for a,b in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                            r,c =i+a, j+b
                            if 0<=r<m and 0<=c<n and (r,c) not in [(3,0), (3,2)]:
                                # print(r,c,k-1)
                                temp+=dp[(r,c,k-1)]
                                    
                    dp[(i,j,k)] = temp
                    count+=temp 
            ans = count
        # print(dp)
        return ans%(10**9+7)
