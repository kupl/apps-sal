class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        max_left = list()
        min_right = list()

        for i in range(len(A)):
            left = A[i]
            if i == 0:
                max_left.append(left)
            elif max_left[i - 1] > left:
                max_left.append(max_left[i - 1])
            else:
                max_left.append(left)

            right = A[len(A) - 1 - i]
            if i == 0:
                min_right.append(right)
            elif min_right[i - 1] < right:
                min_right.append(min_right[i - 1])
            else:
                min_right.append(right)

        for i in range(len(A)):
            if max_left[i] <= min_right[len(A) - i - 2]:
                return i + 1
        return 0
