class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left_maxes = A[:]
        right_mins = A[:]

        for i in range(1, len(left_maxes)):
            if left_maxes[i] < left_maxes[i - 1]:
                left_maxes[i] = left_maxes[i - 1]

        for i in range(len(right_mins) - 2, -1, -1):
            if right_mins[i] > right_mins[i + 1]:
                right_mins[i] = right_mins[i + 1]

        for i in range(1, len(A)):
            if left_maxes[i - 1] <= right_mins[i]:
                return i
