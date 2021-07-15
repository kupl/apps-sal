class Solution:
    def knightDialer(self, n: int) -> int:
        def matmul(A, B):
            BT = list(zip(*B))
            res = [[sum((x*y)%M for x, y in zip(row, col)) for col in BT] for row in A]
            return res
        
        def pow(A, n):
            
            l = n.bit_length()
            res = [[1 if i==j else 0 for j in range(len(A[0]))] for i in range(len(A))]
            tmp = A
            
            for i in range(l):
                
                mask = 1 << i
                
                if mask & n != 0:
                    res = matmul(res, tmp)
                    
                tmp = matmul(tmp, tmp)
                
            return res
        
        M = 10**9+7
        A = [[0,0,0,0,1,0,1,0,0,0],
             [0,0,0,0,0,0,1,0,1,0],
             [0,0,0,0,0,0,0,1,0,1],
             [0,0,0,0,1,0,0,0,1,0],
             [1,0,0,1,0,0,0,0,0,1],
             [0,0,0,0,0,0,0,0,0,0],
             [1,1,0,0,0,0,0,1,0,0],
             [0,0,1,0,0,0,1,0,0,0],
             [0,1,0,1,0,0,0,0,0,0],
             [0,0,1,0,1,0,0,0,0,0]]
        
        res = matmul([[1,1,1,1,1,1,1,1,1,1]], pow(A,n-1))
        
        return sum(res[0]) % M

