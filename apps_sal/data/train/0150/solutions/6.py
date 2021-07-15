class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left = [A[0]]
        for i in range(1, len(A)):
            left.append(max(left[-1], A[i]))
        right = [A[-1]]
        for i in range(len(A) - 2, -1, -1):
            right.append(min(right[-1], A[i]))
        for i in range(1, len(A)):
            if left[i - 1] <= right[-i - 1]:
                return i
            

