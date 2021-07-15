class Solution:
    
    
    def minScoreTriangulation(self, A: List[int]) -> int:
        
        #dp = [[0 for i in range(50)] for j in range(50)]
        dp = dict()
        def helper(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if j-i <= 1:
                dp[(i, j)] = 0
                return dp[(i, j)]
            
            minval = float('inf')
            for k in range(i+1, j):
                #print(i, k, j, A[i]*A[j]*A[k])
                val = helper(i, k) + helper(k, j) + A[i]*A[j]*A[k]
                minval = min(minval, val)
            dp[(i, j)] = minval
            #print(i, j, minval)
            return dp[(i, j)]
        
        return helper(0, len(A)-1)
    
    def minScoreTriangulation3(self, A: List[int]) -> int:
        
        if len(A) < 3:
            return 0
        
        if len(A) == 3:
            return A[0]*A[1]*A[2]
        
        def multi_array(B, j):
            #print(B[j%len(B)],B[(j+1)%len(B)],B[(j+2)%len(B)])
            return B[j%len(B)]*B[(j+1)%len(B)]*B[(j+2)%len(B)]
        
        # 
        sum1, sum2 = 0, 0
        A_copy = A.copy()
        sum1 += multi_array(A, 0)
        A_copy.pop(1)
        sum1 += self.minScoreTriangulation(A_copy)
        
        sum1 += multi_array(A, len(A)-1)
        A.pop(0)
        sum2 += self.minScoreTriangulation(A_copy)
        
        return min(sum1, sum2)
    
    def minScoreTriangulation2(self, A: List[int]) -> int:
        
        if len(A) < 3:
            return 0
        
        if len(A) == 3:
            return A[0]*A[1]*A[2]
        
        def multi_array(B, j):
            print(B[j%len(B)],B[(j+1)%len(B)],B[(j+2)%len(B)])
            return B[j%len(B)]*B[(j+1)%len(B)]*B[(j+2)%len(B)]
        
        # 
        sum1, sum2 = 0, 0
        next_A = []
        for i in range(len(A)//2):
            sum1 += multi_array(A, i*2)
            print(i, sum1, multi_array(A, i*2))
            next_A.append(A[(i*2)%len(A)])
           
        #print(i, i*2, )
        if (i*2+2)%len(A) != 0:
            next_A.append(A[(i*2+2)%len(A)])
            
        print(next_A, sum1)
        sum1 += self.minScoreTriangulation(next_A)
            
        print(sum1, '\
')
        val = A.pop(0)
        A.append(val)
        next_A = []
        for i in range(len(A)//2):
            
            sum2 += multi_array(A, i*2)
            print(i, sum2)
            next_A.append(A[(i*2)%len(A)])
        if (i*2+2)%len(A) != 0:
            next_A.append(A[(i*2+2)%len(A)])
        print(next_A, sum2)
        sum2 += self.minScoreTriangulation(next_A)
        
        return min(sum1, sum2)
