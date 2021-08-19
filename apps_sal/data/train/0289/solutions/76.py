class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        A = [0] + A
        for i in range(1, len(A)):
            A[i] += A[i - 1]

        def solve(l, m, a):
            curr = 0
            for i in range(len(a) - l + 1):
                for j in range(i + l, len(a) - m):
                    temp = a[i + l] - a[i] + a[j + m] - a[j]
                    if temp > curr:
                        curr = temp
            return curr
        m2 = solve(M, L, A)
        m = solve(L, M, A)
        return max(m, m2)
