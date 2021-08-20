class Solution:

    def numberOfArithmeticSlices(self, A):
        (curr, sum) = (0, 0)
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                curr += 1
                sum += curr
            else:
                curr = 0
        return sum
