class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        h = {}
        right = float('inf')

        for j in range(len(A)-1,-1,-1):
            right = min(right, A[j])
            h[j] = right
        
        left = float('-inf')
        for i in range(len(A)-1):
            left = max(left, A[i])
            if left <= h[i+1]:
                return i + 1
        

