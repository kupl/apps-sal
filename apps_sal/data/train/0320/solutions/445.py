class Solution:

    def minOperations(self, A: List[int]) -> int:
        r = 0
        while A != [0 for i in A]:
            odd = 0
            for i in range(len(A)):
                if A[i] % 2 == 1:
                    A[i] = A[i] - 1
                    odd += 1
            if odd == 0:
                A = [x // 2 for x in A]
                r += 1
            else:
                r += odd
        return r
