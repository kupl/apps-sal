class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        
        table=[[-1 for i in range(len(A))] for j in range(len(A))]
    
        def recursion(x=0,y=len(A)-1,A:list=A):
            if y-x<=1:
                return 0
            
            if table[x][y]!=-1:
                return table[x][y]
            else:
                m=float('inf')
                for i in range(x+1,y):
                    m=min(m,recursion(x,i,A)+recursion(i,y,A)+A[x]*A[y]*A[i])
                table[x][y]=m
                return m
        
        return recursion()

