class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
#         dp=[[0 for _ in range(K+1)] for _ in range(N+1)];
        
#         for n in range(N+1):
#             dp[n][0]=float('inf');
            
#         for k in range(K+1):
#             dp[0][k]=0;
            
        
#         for k in range(1,K+1):
#             for n in range(1,N+1):
#                 # res= float('inf');
#                 # for i in range(1,n+1):
#                 #     res= min(res, max(dp[i-1][k-1],dp[n-i][k]));
#                 # dp[n][k]=1+res;
                
#                 l=1;
#                 r=n;
                
#                 while(r-l>=2):
#                     mid=int((l+r)/2);
                    
#                     a= dp[mid-1][k-1];
#                     b= dp[n-mid][k];
                    
#                     if a>b:
#                         r=mid-1;
#                     elif a<b:
#                         l=mid+1;
#                     else:
#                         l,r=mid,mid;
                        
#                 dp[n][k]= 1 + min( max(dp[l-1][k-1],dp[n-l][k]) , max(dp[r-1][k-1],dp[n-r][k]));
                
#         return dp[N][K];



        # O(k*N) time
        
        dp= [[0 for _ in range(K+1)] for _ in range(N+1)];
        
        for n in range(1,N+1):
            for k in range(1,K+1):
                dp[n][k]=1 + dp[n-1][k] + dp[n-1][k-1];
            if dp[n][K]>=N:
                return n;
