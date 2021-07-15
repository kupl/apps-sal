class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        N = len(A)
        maxLeft = dict()
        minRight = dict()
        
        if N == 2 and A[0] <= A[1]:
            return 1

        maxLeft[0] = A[0]
        for i in range(1, N - 1):
            maxLeft[i] = max(maxLeft[i - 1], A[i])
            
        minRight[N - 1] = A[-1]
        for i in range(N - 2, 0, -1):
            minRight[i] = min(minRight[i + 1], A[i])
            
        print({ 'maxLeft': maxLeft })
        print({ 'minRight': minRight })
        
        for i in range(N - 1):
            if maxLeft[i] <= minRight[i + 1]:
                return i + 1
            
        return -1
