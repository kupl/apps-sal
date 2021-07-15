class Solution:
    def knightDialer(self, n: int) -> int:
        #recursive + memo
#         next_map = {0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4]}
       
#         def dfs(cur_num,n):
#             if (cur_num,n) in memo.keys():
#                 return memo[(cur_num,n)]
#             if n == 0:
#                 return 1
#             ans = 0
#             for next_num in next_map[cur_num]:                
#                 ans += dfs(next_num,n-1)
#             memo[(cur_num,n)] = ans
#             return ans
        
#         ans = 0
#         MOD = pow(10,9)+7
#         memo = {}
#         for i in range(10):            
#             ans += dfs(i,n-1)%MOD
#             ans = ans%MOD
#         #    print (\"i:{}, ans={}\".format(i,ans))
            
#         return ans

          #dp[numr][n]: represent the total combinations when start with number :num with n steps
          dp = [ [0 for _ in range(n+1)] for _ in range(10)]
          next_map = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
          MOD = pow(10,9)+7
        
          for i in range(10):
              dp[i][1] = 1
            
          for k in range(2,n+1):
              for i in range(10):
                  for next_num in next_map[i]:
                      dp[i][k] += dp[next_num][k-1]%MOD
                      dp[i][k] %= MOD
          ans  = 0  
          for i in range(10):
              ans += dp[i][n]
              ans %= MOD
            
          return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

