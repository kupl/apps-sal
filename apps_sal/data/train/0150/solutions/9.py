class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left_max = []
        right_min = []
        for i in range(len(A)):
            if i == 0:
                left_max.append(A[i])
            else:
                left_max.append(max(A[i], left_max[-1]))
        for i in range(len(A)-1, -1, -1):
            if i == len(A) - 1:
                right_min.append(A[i])
            else:
                right_min.append(min(A[i], right_min[-1]))
        right_min.reverse()
        
        for i in range(len(A)-1):
            lm = left_max[i]
            rm = right_min[i+1]
            if lm <= rm:
                return i+1

