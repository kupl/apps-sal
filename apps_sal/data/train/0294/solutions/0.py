class Solution:
     def totalNQueens(self, n):
         def dfs(lst, xy_dif, xy_sum):
             p=len(lst)
             if p==n: res.append(lst)
             for q in range(n):
                 if (q not in lst) and (p-q not in xy_dif) and (p+q not in xy_sum):
                     dfs(lst+[q], xy_dif+[p-q], xy_sum +[p+q])
             
         res=[]
         dfs([],[],[])
         return len(res)
