class Solution:
    
    def findKthBit(self, n: int, k: int) -> str:
        
        A = [0]
        
        while k > len(A):
            A.append(1)
            for i in range(len(A)-2,-1,-1):
                A.append(A[i] ^ 1)
                
        return str(A[k-1])
