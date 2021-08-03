class Solution:
    def minOperations(self, A):

        steps, n = 0, len(A)
        while True:
            zeros = 0
            for i in range(n):
                if A[i] % 2 > 0:
                    A[i] -= 1
                    steps += 1
                if A[i] == 0:
                    zeros += 1
            if zeros == n:
                break
            for i in range(n):
                A[i] >>= 1
            steps += 1
        return steps
