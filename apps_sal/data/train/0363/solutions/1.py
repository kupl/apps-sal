class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        self.f = 0
        self.s = set()
        
        m,n = len(A),len(A[0])
        
        def rr(j,i):
            if (j,i) in self.s:
                return
            self.s.add((j,i))
            
            if A[j][i] == 0:
                return
            else:
                for d in dirs:
                    j_new = d[0] + j
                    i_new = d[1] + i
                    if 0 <= j_new < m and 0 <= i_new < n:
                        rr(j_new,i_new)
                        
        for j,row in enumerate(A):
            for i,v in enumerate(row):
                if j == 0 or j == m-1 or i == 0 or i == n-1:
                    rr(j,i)
                    
        f = 0
        for j,row in enumerate(A):
            for i,v in enumerate(row):
                if v == 1 and (j,i) not in self.s:
                    f+=1
                    
        return f
        

