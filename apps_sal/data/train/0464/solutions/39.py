class Solution:

    def minOperations(self, n: int) -> int:
        A = [2 * i + 1 for i in range(n)]
        median = A[len(A) // 2]
        return sum((abs(i - median) for i in A)) // 2
