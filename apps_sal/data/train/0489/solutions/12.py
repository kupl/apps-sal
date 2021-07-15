class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        largest = 0
        
        A = [(index, value) for index, value in enumerate(A)]
        
        A.sort(key=lambda x: x[1])
        
        minimum = float('inf')
        for index, el in A:
            largest = max(largest, index - minimum)
            minimum = min(index, minimum)
                    
        return largest
                

