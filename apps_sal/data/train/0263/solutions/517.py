class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        a_0 = 1
        a_1 = 1
        a_2 = 1
        a_3 = 1
        a_4 = 1
        a_5 = 0
        a_6 = 1
        a_7 = 1
        a_8 = 1
        a_9 = 1
        A = [a_0, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9]

        def count_next_moves(A):
            result = []
            result.append(A[6] + A[4])
            result.append(A[6] + A[8])
            result.append(A[7] + A[9])
            result.append(A[4] + A[8])
            result.append(A[3] + A[9] + A[0])
            result.append(0)
            result.append(A[1] + A[7] + A[0])
            result.append(A[6] + A[2])
            result.append(A[1] + A[3])
            result.append(A[2] + A[4])
            return result
        for i in range(n - 1):
            A = count_next_moves(A)
        result = (sum(A) % ((10**9) + 7))
        return result
