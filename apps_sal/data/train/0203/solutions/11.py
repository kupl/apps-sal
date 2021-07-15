class Solution:
     def paths(self,m,n,a,b,memo):
         if m>a or n>b:
             return 0
         if m==a and n==b:
             return 1
         if str(m)+" "+str(n) not in memo:
             memo[str(m)+" "+str(n)] = self.paths(m+1,n,a,b,memo) + self.paths(m,n+1,a,b,memo)
 
         return memo[str(m)+" "+str(n)]
         
         
     def uniquePaths(self, m, n):
         memo =  dict()
         return(self.paths(0,0,m-1,n-1,memo))
