class Solution:
     def uniquePathsWithObstacles(self, obstacleGrid):
         """
         :type obstacleGrid: List[List[int]]
         :rtype: int
         """
         if len(obstacleGrid)==0 and len(obstacleGrid[0])==0:
             return 1
         if len(obstacleGrid)==0:
             return 0
         
         
         ob=False
         for i in range(len(obstacleGrid)):
             for j in range(len(obstacleGrid[i])):
                 if obstacleGrid[i][j]==1:
                     obstacleGrid[i][j]=None
                     ob=True
                     
         for i in range(len(obstacleGrid)):            
             if obstacleGrid[i][0]==0:
                 obstacleGrid[i][0]=1
             if obstacleGrid[i][0]==None:
                 break
                 
         for i in range(len(obstacleGrid[0])):            
             if obstacleGrid[0][i]==0:
                 obstacleGrid[0][i]=1
             if obstacleGrid[0][i]==None:
                 break
                 
         for i in range(1,len(obstacleGrid)):
             for j in range(1,len(obstacleGrid[i])):
                 if obstacleGrid[i][j]!=None:
                     if obstacleGrid[i-1][j]==None and obstacleGrid[i][j-1]==None:
                         obstacleGrid[i][j]=None
                     elif obstacleGrid[i-1][j]==None and obstacleGrid[i][j-1]!=None:
                         obstacleGrid[i][j]=obstacleGrid[i][j-1]
                     elif obstacleGrid[i-1][j]!=None and obstacleGrid[i][j-1]==None:
                         obstacleGrid[i][j]=obstacleGrid[i-1][j]
                     else:
                         obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                 
         if len(obstacleGrid)==1 or len(obstacleGrid[0])==1:
             if ob:
                 return 0
             else:
                 return 1
         
         if obstacleGrid[-1][-1]==None or obstacleGrid[0][0]==None:
             return 0
         
         return obstacleGrid[-1][-1]
