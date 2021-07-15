class Solution:
    def knightDialer(self, n: int) -> int:
        dp=[1]*10
        dic={0:[4,6],1:[8,6],2:[7,9],3:[4,8],4:[3,9,0],6:[1,7,0],7:[2,6],8:[1,3],9:[2,4]}
        
        
        for i in range(1,n):
            temp=dp
            dp=[0]*10
            for j in range(10):
                if j in dic:
                    for k in dic[j]:
                        dp[k]+=temp[j]
                        dp[k]%=(10**9 + 7)
            
                    
        return sum(dp)%(10**9 + 7)
