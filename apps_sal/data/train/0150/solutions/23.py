class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left = [0] * len(A)
        for i in range(len(A)):
            if i == 0:
                left[i] = A[i]
            else:
                if A[i] > left[i - 1]:
                    left[i] = A[i]
                else:
                    left[i] = left[i - 1]

        A_reversed = A[::-1]
        right = [0] * len(A)
        for i in range(len(A)):
            if i == 0:
                right[i] = A_reversed[i]
            else:
                if A_reversed[i] < right[i - 1]:
                    right[i] = A_reversed[i]
                else:
                    right[i] = right[i - 1]
        right = right[::-1]

        print(left, right)
        for i in range(len(left) - 1):
            if left[i] <= right[i + 1]:
                return i + 1
