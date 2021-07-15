class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        right = 1
        maxLeft = A[0]
        
        sortedRight = sorted(range(right, len(A)), key=lambda k: A[k])
        
        while A[sortedRight[0]] < maxLeft:
            right = sortedRight[0] + 1
            maxLeft = max(A[:right])
            sortedRight = sorted(range(right, len(A)), key=lambda k: A[k])
        
        return right
