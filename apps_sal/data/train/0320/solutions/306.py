class Solution:

    def minOperations(self, A: List[int]) -> int:

        def even(A):
            for i in range(len(A)):
                A[i] //= 2
            return A

        def odd(A):
            c = 0
            z = 0
            for i in range(len(A)):
                if A[i] % 2 == 1:
                    A[i] -= 1
                    c += 1
                    if A[i] == 0:
                        z += 1
            return (A, c, z)
        res = 0
        zero = 0
        for i in A:
            if i == 0:
                zero += 1
        while zero < len(A):
            (A, c, z) = odd(A)
            zero += z
            res += c
            if zero < len(A):
                A = even(A)
                res += 1
        return res
