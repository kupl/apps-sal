class Solution:

    def minOperations(self, n: int) -> int:
        sumz = 0
        for i in range(0, n):
            sumz += 2 * i + 1
        median = sumz // n
        steps = 0
        for i in range(n // 2):
            steps += median - (2 * i + 1)
        return steps
