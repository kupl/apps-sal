class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        max_left = [None] * len(A)
        min_right = [None] * len(A)
        
        m = A[0]
        for i in range(len(A)):
            m = max(m, A[i])
            max_left[i] = m

        m = A[-1]
        for i in range(len(A)-1, -1, -1):
            m = min(m, A[i])
            min_right[i] = m

        for i in range(1, len(A)):
            if max_left[i-1] <= min_right[i]:
                return i
