class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        max_length = 0
        S = set(A)
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                x, y = A[i], A[j]
                expected = x+y
                length = 2
                while expected in S:
                    x=y
                    y=expected
                    expected = x+y
                    length += 1
                
                if length > max_length:
                    max_length = length
                    
        return max_length if max_length >= 3 else 0

