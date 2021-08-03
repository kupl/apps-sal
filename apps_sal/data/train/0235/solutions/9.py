class Solution:
    def __init__(self):
        self.total_sum = 0

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.slices(A, len(A) - 1)
        return self.total_sum

    def slices(self, A, i):
        if i < 2:
            return 0
        temp = 0
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            temp = 1 + self.slices(A, i - 1)
            self.total_sum += temp
        else:
            self.slices(A, i - 1)
        return temp
