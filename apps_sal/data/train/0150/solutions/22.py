class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        max_left = float('-inf')
        min_right = A[-1]
        left = []
        right = [A[-1]]
        
        for i in range(len(A)):
            max_left = max(max_left, A[i])
            left.append(max_left)
            
        for i in range(len(A) - 2, -1, -1):
            min_right = min(min_right, A[i + 1])
            right.append(min_right)
        right.reverse()
        #print(left)
        #print(right)
        for i in range(len(left)):
            if left[i] <= right[i]:
                return i + 1
